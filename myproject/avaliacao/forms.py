from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']
        widgets = {
            'nota': forms.NumberInput(attrs={'min': 1, 'max': 5, 'step': 1}),
            'comentario': forms.Textarea(attrs={'maxlength': 200}),
        }