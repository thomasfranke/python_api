from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']
        widgets = {
            'nota': forms.Select(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'maxlength': 200, 'placeholder': 'Deixe seu comentário', 'class': 'form-control'}),
        }