from django.db import models

class Localizacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    regiao = models.CharField(max_length=100, verbose_name="Região")
    continente = models.CharField(max_length=100, verbose_name="Continente")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Localização"
        verbose_name_plural = "Localizações"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    cpf = models.CharField(max_length=100, verbose_name="CPF")
    email = models.CharField(max_length=100, verbose_name="Email")
    datanasc = models.CharField(max_length=100, verbose_name="Data de nascimento")
    nivel = models.CharField(max_length=100, verbose_name="Nível de acesso")
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, verbose_name="Localização")
    
    def __str__(self):
        return f"{self.nome}, {self.nivel}"
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class LogAtualizacao(models.Model):
    data = models.CharField(max_length=100, verbose_name="Data")
    hora = models.CharField(max_length=100, verbose_name="Hora")
    acao = models.CharField(max_length=100, verbose_name="Ação realizada")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
 
    def __str__(self):
        return f"{self.data} - {self.acao}"
 
    class Meta:
        verbose_name = "Log de Atualização"
        verbose_name_plural = "Logs de Atualização"


class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    site = models.CharField(max_length=100, verbose_name="Site oficial")
    tipo = models.CharField(max_length=100, verbose_name="Tipo de instituição")
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, verbose_name="Localização")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"


class EventoGeopolitico(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    data = models.CharField(max_length=100, verbose_name="Data de início")
    tipo = models.CharField(max_length=100, verbose_name="Tipo de evento")
    areasaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Evento Geopolítico"
        verbose_name_plural = "Eventos Geopolíticos"


class Comentario(models.Model):
    texto = models.CharField(max_length=100, verbose_name="Texto")
    data = models.CharField(max_length=100, verbose_name="Data")
    hora = models.CharField(max_length=100, verbose_name="Hora")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    eventogeopolitico = models.ForeignKey(EventoGeopolitico, on_delete=models.CASCADE, verbose_name="Evento geopolítico")
    
    def __str__(self):
        return f"{self.pessoa.nome}: {self.texto}"
 
    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"


class FonteInformacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    url = models.CharField(max_length=100, verbose_name="URL de referência")
    score = models.CharField(max_length=100, verbose_name="Score de credibilidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Fonte de Informação"
        verbose_name_plural = "Fontes de Informação"


class Commodity(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    preco_base_internacional = models.CharField(max_length=100, verbose_name="Preço base internacional")
    unidade_medida = models.CharField(max_length=100, verbose_name="Unidade de medida")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Commodity"
        verbose_name_plural = "Commodities"


class IndicadorInflacao(models.Model):
    valor_percentual = models.CharField(max_length=100, verbose_name="Valor percentual")
    data = models.CharField(max_length=100, verbose_name="Data de referência")
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, verbose_name="Commodity")
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, verbose_name="Localização")

    def __str__(self):
        return self.valor_percentual

    class Meta:
        verbose_name = "Indicador de Inflação"
        verbose_name_plural = "Indicadores de Inflação"


class FluxoMigratorio(models.Model):
    quantidade = models.CharField(max_length=100, verbose_name="Quantidade estimada")
    justificativa = models.CharField(max_length=100, verbose_name="Justificativa da crise")
    locorigem = models.ForeignKey(Localizacao, on_delete=models.CASCADE, related_name="origem", verbose_name="Localização de origem")
    locdestino = models.ForeignKey(Localizacao, on_delete=models.CASCADE, related_name="destino", verbose_name="Localização de destino")

    def __str__(self):
        return self.quantidade

    class Meta:
        verbose_name = "Fluxo Migratório"
        verbose_name_plural = "Fluxos Migratórios"


class RotaComercial(models.Model):
    nome_hub = models.CharField(max_length=100, verbose_name="Nome do hub")
    status = models.CharField(max_length=100, verbose_name="Status operacional") 
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, verbose_name="Localização")

    def __str__(self):
        return self.nome_hub

    class Meta:
        verbose_name = "Rota Comercial"
        verbose_name_plural = "Rotas Comerciais"


class ImpactoEconomico(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição do impacto")
    prazo = models.CharField(max_length=100, verbose_name="Prazo estimado")
    eventogeopolitico = models.ForeignKey(EventoGeopolitico, on_delete=models.CASCADE, verbose_name="Evento geopolítico")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Impacto Econômico"
        verbose_name_plural = "Impactos Econômicos"


class NexoCausal(models.Model):
    explicacao = models.TextField(max_length=500, verbose_name="Explicação didática")
    estrutura = models.CharField(max_length=100, verbose_name="Estrutura de análise")
    eventogeopolitico = models.ForeignKey(EventoGeopolitico, on_delete=models.CASCADE, verbose_name="Evento geopolítico")
    impactoeconomico = models.ForeignKey(ImpactoEconomico, on_delete=models.CASCADE, verbose_name="Impacto económico")

    def __str__(self):
        return self.explicacao

    class Meta:
        verbose_name = "Nexo Causal"
        verbose_name_plural = "Nexos Causais"


class RelatorioPais(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título do painel")
    data = models.CharField(max_length=100, verbose_name="Data de geração")
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, verbose_name="Localização")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Relatório por País"
        verbose_name_plural = "Relatórios por País"