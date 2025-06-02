from django.db import models

class Usuario(models.Model):
    TIPO_CHOICES = [
        ('aluno', 'Aluno'),
        ('funcionario', 'Funcionario'),
    ]

    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_CHOICES)
    curso = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
