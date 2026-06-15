from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView 
from app.views import (
    IndexView, LoginView, PessoaView, LogAtualizacaoView, ComentarioView,
    LocalizacaoView, InstituicaoView, AreaSaberView, EventoGeopoliticoView,
    FonteInformacaoView, CommodityView, IndicadorInflacaoView,
    FluxoMigratorioView, RotaComercialView, ImpactoEconomicoView,
    NexoCausalView, RelatorioPaisView
)

urlpatterns = [
    # Ajustado para puxar LoginView igual está nas suas views
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # Painel Principal
    path('', IndexView.as_view(), name='index'),
    
    # Admin do Django
    path('admin/', admin.site.urls),
    
    # Demais visualizações do sistema
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