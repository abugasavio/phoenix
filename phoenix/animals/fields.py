from django.utils.safestring import mark_safe
from django.utils.six import text_type
from django_select2.views import NO_ERR_RESP
from django.core.exceptions import ValidationError
from django_select2.widgets import AutoHeavySelect2Widget
from django_select2.fields import AutoSelect2MultipleField, AutoModelSelect2Field, AutoModelSelect2TagField
from django.utils.html import format_html
from django.forms.utils import flatatt, force_text
from .models import Animal, Color, Breed, Breeder, Sire, Dam


class MultipleAnimalsField(AutoSelect2MultipleField):
    def get_results(self, request, term, page, context):
        # Fetch all by default
        animals = Animal.objects.all()

        # If there's actually a term, filter on it
        if term.strip() != '':
            animals = animals.filter(name__icontains=term)

        res = [(animal.id, animal.name) for animal in animals]
        return (NO_ERR_RESP, False, res)  # Any error response, Has more results, options list


class BullField(AutoModelSelect2Field):
    queryset = Sire.objects.all()
    search_fields = ['name__icontains']
    to_field = 'name'


class CowField(AutoModelSelect2Field):
    queryset = Dam.objects.all()
    search_fields = ['name__icontains']
    to_field = 'name'


class ColorField(AutoModelSelect2Field):
    queryset = Color.objects
    search_fields = ['name__icontains']
    to_field = 'name'


class BreederField(AutoModelSelect2Field):
    queryset = Breeder.objects
    search_fields = ['name__icontains']
    to_field = 'name'
