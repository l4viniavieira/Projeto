from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoas/', PessoaView.as_view(), name='pessoas'),
    path('logs/', LogAtualizacaoView.as_view(), name='logs'),
    path('comentarios/', ComentarioView.as_view(), name='comentarios'),
    path('localizacoes/', LocalizacaoView.as_view(), name='localizacoes'),
    path('instituicoes/', InstituicaoView.as_view(), name='instituicoes'),
    path('areassaber/', AreaSaberView.as_view(), name='areassaber'),
    path('eventos/', EventoGeopoliticoView.as_view(), name='eventosgeopoliticos'),
    path('fontes/', FonteInformacaoView.as_view(), name='fontesinformacao'),
    path('commodities/', CommodityView.as_view(), name='commodities'),
    path('inflacao/', IndicadorInflacaoView.as_view(), name='indicadoresinflacao'),
    path('migracoes/', FluxoMigratorioView.as_view(), name='fluxosmigratorios'),
    path('rotascomerciais/', RotaComercialView.as_view(), name='rotascomerciais'),
    path('impactos/', ImpactoEconomicoView.as_view(), name='impactos'),
    path('nexoscausais/', NexoCausalView.as_view(), name='nexoscausais'),
    path('relatorios/', RelatorioPaisView.as_view(), name='relatorios'),
]