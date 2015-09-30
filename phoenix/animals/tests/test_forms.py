from datetime import date
from django.test import TestCase
from phoenix.animals.forms import AnimalForm
from phoenix.animals.models import Animal


class AnimalFormTestCase(TestCase):
    def test_valid_form(self):
        form = AnimalForm({
            'ear_tag': '102M',
            'sex': Animal.SEX_CHOICES.female,
            'birth_date': date.today(),
            'name': 'sasa',
        })
        self.assertFalse(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = AnimalForm({})
        self.assertEqual(form.errors,
                         {'birth_date': [u'This field is required.'], 'name': [u'This field is required.'], 'ear_tag': [u'This field is required.'], 'sex': [u'This field is required.']})
