from flask import Flask, render_template, Response, jsonify
import cv2
from CV3T import recognize_plate
import time
from database import get_connection, release_connection, init_db
from concurrent.futures import ThreadPoolExecutor
import threading

app = Flask(__name__)
camera = cv2.VideoCapture(0)

# Configura a resolução da câmera (pode testar 320x240 se precisar de mais FPS)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Thread pool para inserções assíncronas
executor = ThreadPoolExecutor(max_workers=2)
frame_count = 0
last_plate = None

def buscar_ultimo_status(placa):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT status FROM placas_placadetectada
                WHERE placa = %s
                ORDER BY data_hora DESC
                LIMIT 1
                """,
                (placa,)
            )
            result = cur.fetchone()
            if result:
                return result[0]
            else:
                return None
    finally:
        release_connection(conn)

def determinar_status(placa):
    ultimo_status = buscar_ultimo_status(placa)
    if ultimo_status == 'entrada':
        return 'saida'
    return 'entrada'

def save_plate_to_db(plate, status):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO placas_placadetectada (placa, data_hora, status)
                VALUES (%s, %s, %s)
                RETURNING id
                """,
                (plate, time.strftime("%Y-%m-%d %H:%M:%S"), status)
            )
            plate_id = cur.fetchone()[0]
        conn.commit()
        print(f"Placa inserida com sucesso! ID: {plate_id}, status: {status}")
        return plate_id
    except Exception as e:
        conn.rollback()
        print(f"Erro ao salvar placa: {e}")
        raise
    finally:
        release_connection(conn)

def save_plate_to_db_async(plate, status):
    executor.submit(save_plate_to_db, plate, status)

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    global last_plate, frame_count
    while True:
        success, frame = camera.read()
        if not success:
            break

        # redimensiona para performance
        frame = cv2.resize(frame, (640, 480))
        frame_count += 1

        plate = None
        # rodar OCR a cada 15 frames
        if frame_count % 15 == 0:
            plate = recognize_plate(frame)

        if plate and plate != last_plate:
            status = determinar_status(plate)
            last_plate = plate
            save_plate_to_db_async(plate, status)
            registrar_entrada_ou_saida(plate, status)
            cv2.putText(
                frame,
                f"Placa: {plate} ({status})",
                (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
                cv2.LINE_AA
            )

        ret, buf = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buf.tobytes() + b'\r\n')
        time.sleep(0.03)

# Dicionário para armazenar o tempo de entrada de cada placa
placas_em_monitoramento = {}  # {placa: tempo_entrada}
placas_tempos = []  # Lista de registros: [{'placa': ..., 'entrada': ..., 'saida': ..., 'tempo_total': ...}]

lock = threading.Lock()  # Para evitar condições de corrida

def registrar_entrada_ou_saida(placa, status):
    now = time.time()
    with lock:
        if status == 'entrada':
            placas_em_monitoramento[placa] = now
        elif status == 'saida' and placa in placas_em_monitoramento:
            entrada = placas_em_monitoramento.pop(placa)
            tempo_total = now - entrada
            placas_tempos.append({
                'placa': placa,
                'entrada': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entrada)),
                'saida': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now)),
                'tempo_total_segundos': round(tempo_total, 2)
            })

# Para consultar os tempos pelo Flask:
@app.route('/placas_tempos')
def get_placas_tempos():
    with lock:
        return jsonify(placas_tempos)
    
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/last_plate')
def get_last_plate():
    return jsonify({'plate': last_plate})

@app.route('/get_all_plates')
def get_all_plates():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, placa, data_hora, status
                FROM placas_placadetectada
                ORDER BY data_hora DESC
        """)
            rows = cur.fetchall()
        plates = [
            {
                'id': row[0],
                'placa': row[1],
                'data_hora': row[2].strftime('%Y-%m-%d %H:%M:%S'),
                'status': row[3]
            }
            for row in rows
        ]
        return jsonify(plates)
    finally:
        release_connection(conn)
        
if __name__ == '__main__':
    init_db()
    app.run(debug=False)
