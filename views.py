from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

class LogAtualizacaoView(View):
    def get(self, request, *args, **kwargs):
        logs = LogAtualizacao.objects.all()
        return render(request, 'logatualizacao.html', {'logs': logs})

class ComentarioView(View):
    def get(self, request, *args, **kwargs):
        comentarios = Comentario.objects.select_related('eventogeopolitico')
        return render(request, 'comentario.html', {'comentarios': comentarios})

class LocalizacaoView(View):
    def get(self, request, *args, **kwargs):
        localizacoes = Localizacao.objects.all()
        return render(request, 'localizacao.html', {'localizacoes': localizacoes})

class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})

class AreaSaberView(View):
    def get(self, request, *args, **kwargs):
        areassaber = AreaSaber.objects.all()
        return render(request, 'areasaber.html', {'areas_saber': areassaber})

class EventoGeopoliticoView(View):
    def get(self, request, *args, **kwargs):
        eventos = EventoGeopolitico.objects.select_related('areasaber')
        return render(request, 'eventogeopolitico.html', {'eventos': eventos})

class FonteInformacaoView(View):
    def get(self, request, *args, **kwargs):
        fontes = FonteInformacao.objects.all()
        return render(request, 'fonteinformacao.html', {'fontes': fontes})

class CommodityView(View):
    def get(self, request, *args, **kwargs):
        commodities = Commodity.objects.all()
        return render(request, 'commodity.html', {'commodities': commodities})

class IndicadorInflacaoView(View):
    def get(self, request, *args, **kwargs):
        indicadores = IndicadorInflacao.objects.all()
        return render(request, 'indicadorinflacao.html', {'indicadores': indicadores})

class FluxoMigratorioView(View):
    def get(self, request, *args, **kwargs):
        fluxos = FluxoMigratorio.objects.select_related('locorigem', 'locdestino')
        return render(request, 'fluxomigratorio.html', {'fluxos': fluxos})

class RotaComercialView(View):
    def get(self, request, *args, **kwargs):
        rotascomerciais = RotaComercial.objects.all()
        return render(request, 'rotacomercial.html', {'rotas': rotascomerciais})

class ImpactoEconomicoView(View):
    def get(self, request, *args, **kwargs):
        impactos = ImpactoEconomico.objects.all()
        return render(request, 'impactoeconomico.html', {'impactos': impactos})

class NexoCausalView(View):
    def get(self, request, *args, **kwargs):
        nexos = NexoCausal.objects.all()
        return render(request, 'nexocausal.html', {'nexoscausais': nexos})

class RelatorioPaisView(View):
    def get(self, request, *args, **kwargs):
        relatorios = RelatorioPais.objects.all()
        return render(request, 'relatoriopais.html', {'relatorios': relatorios})