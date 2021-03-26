from django.contrib import admin
from django.urls import path
from cadastro.views import *

urlpatterns = [
    path("registrar-pessoa/", registrar_pessoa, name="registrar_pessoa"),
    path("registrar-votacao/", registrar_votacao, name="registrar_votacao"),
    path("registrar-opcao-voto/", registrar_opcao, name="registrar_opcao"),
    path("listar-pessoas/", listar_pessoas, name="listar_pessoas"),

    path("votar/<int:id_votacao>", votar, name="votar"),
    path("validar_cpf/<int:id>", validar_cpf, name="validar_cpf"),
]