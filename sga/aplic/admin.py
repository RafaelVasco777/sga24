from django.contrib import admin

from .models import Imovel, Cliente, Contrato, Pagamento, Proprietario

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'tipo', 'preco_aluguel', 'disponivel')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'cliente', 'data_inicio', 'data_fim', 'ativo')

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'data_pagamento', 'valor', 'confirmado')

@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')
