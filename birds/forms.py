from django.forms import ModelForm, modelformset_factory
from .models import Bird


class BirdForm(ModelForm):
    class Meta:
        model = Bird
        fields = ['common_name', 'scientific_name']


BirdFormSet = modelformset_factory(
    Bird, fields=('common_name', 'scientific_name'), extra=1
)
