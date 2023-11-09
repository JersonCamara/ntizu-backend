from django.db import models

# Create your models here.

class CandidatoModel(models.Model): 
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    profissao = models.CharField(max_length=150)
    cell = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class EmpresaModel(models.Model): 
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    cell = models.CharField(max_length=50)
    nuit = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
