from django import forms
from django.contrib.postgres.fields import ArrayField
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['previews'].widget = forms.widgets.Textarea(
            attrs={'rows': 3, 'cols': 40}
        )