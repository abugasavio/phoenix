from django import forms
from django.utils.safestring import mark_safe
from bootstrap3_datetime.widgets import DateTimePicker
from django_select2.fields import Select2ChoiceField
from django_select2.widgets import AutoHeavySelect2Widget, Select2Widget, AutoHeavySelect2TagWidget, HeavySelect2TagWidget
from .models import Animal, Service, PregnancyCheck, MilkProduction, Sire, Dam
from .fields import BullField, CowField, ColorField, BreederField


class AnimalForm(forms.ModelForm):
    sex = Select2ChoiceField(choices=Animal.SEX_CHOICES, widget=Select2Widget(select2_options={'minimumInputLength': 0}))
    color = ColorField(required=False, widget=AutoHeavySelect2Widget(select2_options={'minimumInputLength': 0}))
    sire = BullField(required=False, widget=AutoHeavySelect2Widget(select2_options={'minimumInputLength': 0, 'width': '40px'}),
                     attrs={'add_button':mark_safe('<button id="comment-button" class="btn btn-primary" type="button"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Add Category</button>')})
    dam = CowField(required=False, widget=AutoHeavySelect2Widget(select2_options={'minimumInputLength': 0}), help_text='')
    breeder = BreederField(required=False, widget=AutoHeavySelect2Widget(select2_options={'minimumInputLength': 0}))
    birth_date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}))
    weaning_date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}), required=False)
    yearling_date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}), required=False)

    def __init__(self, *args, **kwargs):
        super(AnimalForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ('group', 'sire', 'dam'):
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Animal
        fields = ('ear_tag', 'name', 'color', 'sex', 'breed', 'sire', 'dam', 'breeder',
                  'birth_date', 'birth_weight', 'weaning_date', 'weaning_weight', 'yearling_date',
                  'yearling_weight')


class ServiceForm(forms.ModelForm):
    sire = BullField(widget=AutoHeavySelect2Widget(select2_options={'minimumInputLength': 0}))
    date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}), required=False)

    class Meta:
        model = Service
        fields = ('method', 'sire', 'date', 'notes')


class SireForm(forms.ModelForm):
    birth_date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}))

    class Meta:
        model = Sire
        fields = ('name', 'breed', 'birth_date', 'breeder')


class DamForm(forms.ModelForm):
    birth_date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}))

    class Meta:
        model = Dam
        fields = ('name', 'breed', 'birth_date', 'breeder')


class PregnancyCheckForm(forms.ModelForm):
    date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}))

    class Meta:
        model = PregnancyCheck
        fields = ('service', 'result', 'check_method', 'date',)


class MilkProductionForm(forms.ModelForm):
    date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}))

    class Meta:
        model = MilkProduction
        fields = ( 'animal', 'date', 'time', 'amount', 'butterfat',)
