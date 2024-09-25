import uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

# Função para gerar um nome único para os arquivos
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Modelo de Imóvel
class Imovel(models.Model):
    endereco = models.CharField(_('Endereço'), max_length=255)
    tipo = models.CharField(_('Tipo'), max_length=50, choices=[
        ('Apartamento', _('Apartamento')),
        ('Casa', _('Casa')),
        ('Comercial', _('Comercial')),
    ])
    preco_aluguel = models.DecimalField(_('Preço do Aluguel'), max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(_('Disponível'), default=True)
    imagem = StdImageField(_('Imagem do Imóvel'), null=True, blank=True, upload_to=get_file_path,
                           variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})

    class Meta:
        verbose_name = _('Imóvel')
        verbose_name_plural = _('Imóveis')

    def __str__(self):
        return f"{self.tipo} - {self.endereco}"

# Modelo de Cliente
class Cliente(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    email = models.EmailField(_('E-mail'), unique=True)
    telefone = models.CharField(_('Telefone'), max_length=20)
    foto = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path,
                         variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

    def __str__(self):
        return self.nome

# Modelo de Contrato
class Contrato(models.Model):
    imovel = models.ForeignKey(Imovel, verbose_name=_('Imóvel'), on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, verbose_name=_('Cliente'), on_delete=models.CASCADE)
    data_inicio = models.DateField(_('Data de Início'))
    data_fim = models.DateField(_('Data de Fim'))
    ativo = models.BooleanField(_('Ativo'), default=True)

    class Meta:
        verbose_name = _('Contrato')
        verbose_name_plural = _('Contratos')

    def __str__(self):
        return f"Contrato {self.imovel} - {self.cliente}"

# Modelo de Pagamento
class Pagamento(models.Model):
    contrato = models.ForeignKey(Contrato, verbose_name=_('Contrato'), on_delete=models.CASCADE)
    data_pagamento = models.DateField(_('Data do Pagamento'))
    valor = models.DecimalField(_('Valor'), max_digits=10, decimal_places=2)
    confirmado = models.BooleanField(_('Confirmado'), default=False)

    class Meta:
        verbose_name = _('Pagamento')
        verbose_name_plural = _('Pagamentos')

    def __str__(self):
        return f"Pagamento de {self.valor} em {self.data_pagamento}"

# Modelo de Proprietário
class Proprietario(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    telefone = models.CharField(_('Telefone'), max_length=20)
    email = models.EmailField(_('E-mail'), unique=True)
    foto = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path,
                         variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = _('Proprietário')
        verbose_name_plural = _('Proprietários')

    def __str__(self):
        return self.nome
