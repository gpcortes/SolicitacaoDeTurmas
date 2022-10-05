from multiselectfield import MultiSelectField
from django.db import models


class DefaultTable(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Eixo(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
      managed = False
      db_table = 'eixos'


class Curso(models.Model):
    id = models.IntegerField(primary_key=True)
    curso = models.CharField(max_length=255, null=False, blank=False)
    tipo_id = models.IntegerField(null=False, blank=False)
    eixos_id = models.IntegerField(null=False, blank=False)
    status = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.curso

    class Meta:
      managed = False
      db_table = 'qualificacoes'


class Escola(models.Model):
    id = models.IntegerField(primary_key=True)
    escola = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.escola

    class Meta:
      managed = False
      db_table = 'escolas'


class SolicitacaoDeTurma(DefaultTable):

    TIPOS = (
        ('CAPACITACAO', 'Capacitação'),
        ('QUALIFICACAO', 'Qualificação'),
        ('TECNICO', 'Técnico'),
        ('SUPERIOR', 'Superior'),
    )

    MODALIDADES = (
        ('PRESENCIAL', 'Presencial'),
        ('ONLINE', 'Online'),
        ('EAD', 'EAD'),
    )

    TURNOS = (
        ('MATUTINO', 'Matutino'),
        ('VESPERTINO', 'Vespertino'),
        ('NOTURNO', 'Noturno'),
    )

    TRIMESTRES = (
        ('PRIMEIRO', 'Primeiro'),
        ('SEGUNDO', 'Segundo'),
        ('TERCEIRO', 'Terceiro'),
        ('QUARTO', 'Quarto'),
    )

    SIM_NAO = (
        ('SIM', 'Sim'),
        ('NAO', 'Não'),
    )

    DIAS_SEMANA = (
        ('DOMINGO', 'Domingo'),
        ('SEGUNDA', 'Segunda'),
        ('TERCA', 'Terça'),
        ('QUARTA', 'Quarta'),
        ('QUINTA', 'Quint'),
        ('SEXTA', 'Sexta'),
        ('SABADO', 'Sábado'),
    )

    instace_id = models.CharField(max_length=40, null=True, blank=True)
    escola = models.ForeignKey(Escola, on_delete=models.DO_NOTHING)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    eixo = models.ForeignKey(Eixo, on_delete=models.DO_NOTHING)
    tipo = models.CharField(max_length=255, null=False, blank=False,
                            choices=TIPOS)
    modalidade = models.CharField(max_length=255, null=False, blank=False,
                                  choices=MODALIDADES)
    turno = models.CharField(max_length=255, null=False, blank=False,
                             choices=TURNOS)
    carga_horaria = models.IntegerField(null=False, blank=False)
    vagas = models.IntegerField(null=False, blank=False)
    fluxo_continuo = models.CharField(
        max_length=255, null=False, blank=False, choices=SIM_NAO)
    previsao_inicio = models.DateField(
        max_length=255, null=False, blank=False)
    previsao_fim = models.DateField(max_length=255, null=False, blank=False)
    dias_semana = MultiSelectField(max_length=255, null=False, blank=False,
                                   choices=DIAS_SEMANA)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
      managed = True
      db_table = 'solicitacaodeturma'
