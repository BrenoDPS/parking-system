# Sistema de Estacionamento e Reconhecimento Automatizado de Placas de Veículos com Python

Este projeto realiza o reconhecimento automatizado de placas de veículos utilizando Python, OpenCV e Tesseract OCR. As placas detectadas são salvas em um banco de dados PostgreSQL para uso de um sistema de gerenciamento de veículos e usuários, de forma semelhante a um estacionamento.

---

## **Requisitos do Sistema**
Antes de começar, certifique-se de que o sistema atende aos seguintes requisitos:
- **Sistema Operacional:** Windows 10 ou superior
- **Python:** Versão 3.8 ou superior
- **Tesseract OCR:** Instalado no sistema
- **PostgreSQL:** Conta configurada e banco de dados criado

---

## **Passo a Passo para Configuração**

### **1. Clone o Repositório**
Baixe o código do projeto para o seu computador:
```bash
git clone https://github.com/seu-repositorio/parking-system.git
cd parking-system

2. Instale o Python
Baixe o Python no site oficial: https://www.python.org/downloads/
Durante a instalação, marque a opção "Add Python to PATH".
Verifique a instalação

python --version

3. Crie um Ambiente Virtual
Crie um ambiente virtual para isolar as dependências do projeto:

python -m venv venv

Ative o ambiente virtual:

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

4. Instale as Dependências
Instale as bibliotecas necessárias listadas no arquivo requirements.txt:

pip install -r requirements.txt

Se o arquivo requirements.txt não existir, instale manualmente as dependências:

pip install flask opencv-python pytesseract psycopg2-binary numpy

Bibliotecas utilizadas:

Numpy: Para manipulação de arrays e operações matemáticas.
OpenCV (cv2): Para processamento de imagens e detecção de contornos.
Regex: Para validação de padrões de texto (placas).
Flask: Para criar o servidor web.
Psycopg2-binary: Para conectar e interagir com o PostgreSQL.
Pytesseract: Para reconhecimento óptico de caracteres (OCR).

5. Instale o Tesseract OCR
Baixe o Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki

Durante a instalação, anote o caminho onde o Tesseract foi instalado (exemplo: C:\Program Files\Tesseract-OCR).

Verifique a instalação:

tesseract --version

Atualize o caminho do Tesseract no arquivo CV3T.py:
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

6. - Instale o PostgreSQL: https://www.postgresql.org/download/
- Crie um banco de dados e um usuário para o projeto.
- Anote o nome do banco, usuário, senha, host e porta.

Atualize o arquivo `app.py` com as informações de conexão:
"
import psycopg2

conn = psycopg2.connect(
    dbname='nome_do_banco',
    user='seu_usuario',
    password='sua_senha',
    host='localhost',
    port='5432'
)
"

7. Execute o Projeto
Inicie o servidor Flask:
"bash
python app.py
"

Abra o navegador e acesse:

http://127.0.0.1:5000

8. Teste o Reconhecimento de Placas
Aponte a câmera para uma placa de veículo.
O sistema exibirá o feed de vídeo e detectará as placas.
As placas detectadas serão salvas no MongoDB.

reconhecimento-placas/
│
├── backend/
│   ├── app.py               # Código principal do servidor Flask
│   ├── CV3T.py              # Função de reconhecimento de placas
│   ├── templates/
│   │   └── index.html       # Interface web para exibir o feed de vídeo
│   └── static/              # Arquivos estáticos (CSS, JS, etc.)
│
├── [dados.csv](http://_vscodecontentref_/1)                # Arquivo CSV para salvar placas (opcional)
├── requirements.txt         # Lista de dependências do projeto
└── [README.md](http://_vscodecontentref_/2)                # Documentação do projeto

Problemas Comuns
1. O Tesseract não está funcionando
Verifique se o caminho do Tesseract está correto no arquivo CV3T.py:

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

2. O PostgreSQL não está conectado  
- Certifique-se de que as informações de conexão no `app.py` estão corretas.
- Verifique se o serviço do PostgreSQL está ativo.

3. O feed de vídeo está travando
Reduza a resolução do vídeo no app.py

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

Contribuidores
Diego Justino da Silva (Justas): Desenvolvimento do sistema de reconhecimento de placas.
Breno de Pádua Soares: Desenvolvimento do sistema de gerenciamento de usuários (backend) e integração com o sistema de reconhecimento de placas.
Lucas de Moraes Silveira: Desenvolvimento do sistema de gerenciamento de usuários (frontend).

Licença
Este projeto é de uso acadêmico e não deve ser utilizado para fins comerciais sem autorização.