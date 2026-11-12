from django.contrib import admin
from .models import (
    Localizacao, Pessoa, LogAtualizacao, Instituicao, AreaSaber,
    EventoGeopolitico, Comentario, FonteInformacao, Commodity,
    IndicadorInflacao, FluxoMigratorio, RotaComercial,
    ImpactoEconomico, NexoCausal, RelatorioPais
)


class LogAtualizacaoInline(admin.TabularInline):
    model = LogAtualizacao
    extra = 1


class ComentarioPessoaInline(admin.TabularInline):
    """Exibe os comentários que a pessoa fez dentro da página dela"""
    model = Comentario
    extra = 1
    fk_name = 'pessoa'  


class ComentarioEventoInline(admin.TabularInline):
    """Exibe os comentários vinculados ao evento dentro da página do evento"""
    model = Comentario
    extra = 1
    fk_name = 'eventogeopolitico'


class ImpactoEconomicoInline(admin.StackedInline):
    """Exibe os impactos econômicos dentro da página do evento geopolítico"""
    model = ImpactoEconomico
    extra = 1


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel', 'email')
    search_fields = ('nome', 'cpf')
    inlines = [LogAtualizacaoInline, ComentarioPessoaInline]


class EventoGeopoliticoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'areasaber')
    search_fields = ('titulo', 'descricao')
    inlines = [ImpactoEconomicoInline, ComentarioEventoInline]

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(EventoGeopolitico, EventoGeopoliticoAdmin)

admin.site.register(Localizacao)
admin.site.register(Instituicao)
admin.site.register(AreaSaber)
admin.site.register(FonteInformacao)
admin.site.register(Commodity)
admin.site.register(IndicadorInflacao)
admin.site.register(FluxoMigratorio)
admin.site.register(RotaComercial)
admin.site.register(NexoCausal)
admin.site.register(RelatorioPais)