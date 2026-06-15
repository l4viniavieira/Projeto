from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from .models import *

class LoginView(DjangoLoginView):
    """
    Controlador responsável por renderizar a interface de autenticação
    e gerenciar a validação segura de sessões dos usuários.
    """
    template_name = 'login.html'


class IndexView(LoginRequiredMixin, View):
    """
    Controlador da página inicial que centraliza e exibe o monitor 
    de nexos causais globais apenas para usuários autenticados.
    """
    def get(self, request, *args, **kwargs):
        # Buscamos apenas os eventos geopolíticos trazendo a área do saber integrada
        eventos = EventoGeopolitico.objects.select_related('areasaber').order_by('-id')
        
        painel_conexoes = []
        
        for evento in eventos:
            # Filtra os impactos econômicos amarrados a este evento específico
            impactos = ImpactoEconomico.objects.filter(eventogeopolitico=evento)
            
            # Filtra a explicação didática do nexo causal e traz o impacto econômico acoplado
            nexos = NexoCausal.objects.filter(eventogeopolitico=evento).select_related('impactoeconomico')
            
            # Busca os comentários dos estudantes associados a este evento específico
            comentarios = Comentario.objects.filter(eventogeopolitico=evento).select_related('pessoa')
            
            # Colocamos apenas o que pertence legitimamente a este evento no dicionário
            painel_conexoes.append({
                'evento': evento,
                'impactos': impactos,
                'nexos': nexos,
                'comentarios': comentarios
            })
            
        return render(request, 'index.html', {'painel_conexoes': painel_conexoes})


class PessoaView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})


class LogAtualizacaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logs = LogAtualizacao.objects.all()
        return render(request, 'logatualizacao.html', {'logs': logs})


class ComentarioView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        comentarios = Comentario.objects.select_related('eventogeopolitico')
        return render(request, 'comentario.html', {'comentarios': comentarios})


class LocalizacaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        localizacoes = Localizacao.objects.all()
        return render(request, 'localizacao.html', {'localizacoes': localizacoes})


class InstituicaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})


class AreaSaberView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        areassaber = AreaSaber.objects.all()
        return render(request, 'areasaber.html', {'areas_saber': areassaber})


class EventoGeopoliticoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        eventos = EventoGeopolitico.objects.select_related('areasaber')
        return render(request, 'eventogeopolitico.html', {'eventos': eventos})


class FonteInformacaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        fontes = FonteInformacao.objects.all()
        return render(request, 'fonteinformacao.html', {'fontes': fontes})


class CommodityView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        commodities = Commodity.objects.all()
        return render(request, 'commodity.html', {'commodities': commodities})


class IndicadorInflacaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        indicadores = IndicadorInflacao.objects.all()
        return render(request, 'indicadorinflacao.html', {'indicadores': indicadores})


class FluxoMigratorioView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        fluxos = FluxoMigratorio.objects.select_related('locorigem', 'locdestino')
        return render(request, 'fluxomigratorio.html', {'fluxos': fluxos})


class RotaComercialView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        rotascomerciais = RotaComercial.objects.all()
        return render(request, 'rotacomercial.html', {'rotas': rotascomerciais})


class ImpactoEconomicoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        impactos = ImpactoEconomico.objects.all()
        return render(request, 'impactoeconomico.html', {'impactos': impactos})


class NexoCausalView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        nexos = NexoCausal.objects.all()
        return render(request, 'nexocausal.html', {'nexoscausais': nexos})


class RelatorioPaisView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        relatorios = RelatorioPais.objects.all()
        return render(request, 'relatoriopais.html', {'relatorios': relatorios})