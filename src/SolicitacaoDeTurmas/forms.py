from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .widgets import DatePickerInput
from .models import SolicitacaoDeTurma


class SolicitacaoDeTurmas(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SolicitacaoDeTurmas, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('escola', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('eixo', css_class='form-group col-md-4 mb-0'),
                Column('curso', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('tipo', css_class='form-group col-md-4 mb-0'),
                Column('modalidade', css_class='form-group col-md-4 mb-0'),
                Column('turno', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('carga_horaria', css_class='form-group col-md-4 mb-0'),
                Column('vagas', css_class='form-group col-md-4 mb-0'),
                Column('fluxo_continuo', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('previsao_inicio', css_class='form-group col-md-3 mb-0'),
                Column('previsao_fim', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row('dias_semana', css_class='form-group col-md-3 mb-0'),
        )
        self.helper.layout.append(Submit('save', 'Salvar'))
        
    class Meta:
        model = SolicitacaoDeTurma
        
        fields = (
            'escola',
            'curso',
            'eixo',
            'tipo',
            'modalidade',
            'turno',
            'carga_horaria',
            'vagas',
            'fluxo_continuo',
            'previsao_inicio',
            'previsao_fim',
            'dias_semana',
        )
        
        labels = {
            'escola': 'Escola',
            'curso': 'Curso',
            'eixo': 'Eixo',
            'tipo': 'Tipo',
            'modalidade': 'Modalidade',
            'turno': 'Turno',
            'carga_horaria': 'Carga horária',
            'vagas': 'Vagas',
            'fluxo_continuo': 'Fluxo contínuo',
            'previsao_inicio': 'Previsão de inínio',
            'previsao_fim': 'Previsão de fim',
            'dias_semana': 'Dias da Semana',
        }
        
        widgets = {
            'previsao_inicio': DatePickerInput(),
            'previsao_fim': DatePickerInput(),
        }