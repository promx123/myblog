from django import forms
from .models import Entry

class CrearEntradaForm(forms.ModelForm):
    """Form definition for CrearEntradaForm."""

    class Meta:
        """Meta definition for CrearEntradaFormform."""

        model = Entry
        fields = ('__all__')
