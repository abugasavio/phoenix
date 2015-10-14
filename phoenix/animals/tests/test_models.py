import pytest
from django.test import TestCase
from model_mommy import mommy
from phoenix.animals.models import Animal, Dam, Sire
from phoenix.utils import test_utils

pytestmark = pytest.mark.django_db


class AnimalTestCase(TestCase):
    def setUp(self):
        self.dam = mommy.make('animals.Animal', ear_tag='456', name='dam', sex=Animal.SEX_CHOICES.female)
        self.sire = mommy.make('animals.Animal', ear_tag='123', name='sire', sex=Animal.SEX_CHOICES.male)

    def test_transitions(self):
        self.assertEqual('open', self.dam.state)
        self.dam.open()
        self.dam.save()
        self.assertEqual('open', self.dam.state)
        self.dam.served()
        self.dam.save()
        self.assertEqual('served', self.dam.state)
        self.dam.pregnant()
        self.dam.save()
        self.assertEqual('pregnant', self.dam.state)
        self.dam.lactating()
        self.dam.save()
        self.assertEqual('lactating', self.dam.state)
        self.dam.disposed()
        self.dam.save()
        self.assertEqual('disposed', self.dam.state)

    def test_creating_dam_or_sire(self):
        user = test_utils.create_logged_in_user(self)
        tim = Animal.objects.create(name='tim', ear_tag='123TIM', sex=Animal.SEX_CHOICES.male, created_by=user, modified_by=user)
        sire_tim = Sire.objects.get(animal=tim)
        self.assertEqual(sire_tim.name, 'tim')
