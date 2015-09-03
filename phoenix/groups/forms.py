from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from django_select2.fields import Select2ChoiceField
from django_select2.widgets import AutoHeavySelect2Widget, Select2Widget
from phoenix.animals.models import Animal
from phoenix.animals.fields import BreedField, BullField, CowField
from .models import Group


class GroupForm(forms.ModelForm):
    sex = Select2ChoiceField(required=False, choices=Animal.SEX_CHOICES, widget=Select2Widget(select2_options={'minimumInputLength': 0}))
    breed = BreedField(required=False, widget=AutoHeavySelect2Widget(select2_options={'minimumInputLength': 0}))
    start_birth_date = forms.DateField(required=False, widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}))
    end_birth_date = forms.DateField(required=False, widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}))
    sire = BullField(required=False, widget=AutoHeavySelect2Widget(select2_options={'minimumInputLength': 0}))
    dam = CowField(required=False, widget=AutoHeavySelect2Widget(select2_options={'minimumInputLength': 0}))

    class Meta:
        model = Group
        exclude = ('is_active', 'created_by', 'created_on', 'modified_by', 'modified_on')