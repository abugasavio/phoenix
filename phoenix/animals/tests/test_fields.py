from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from model_mommy import mommy
from phoenix.animals.models import Animal
from phoenix.animals.fields import MultipleAnimalsField, BullField


class AnimalFieldTestCase(TestCase):

    def setUp(self):
        self.dam = mommy.make('animals.Dam', name='dam')
        self.sire = mommy.make('animals.Sire', name='sire')
        self.animal = mommy.make('animals.Animal', ear_tag='tagie', name='tagie', sex=Animal.SEX_CHOICES.male)
        self.factory = RequestFactory()

    def test_multiple_animal_field(self):
        request = self.factory.get(reverse('django_select2_central_json'))
        # result looks like this: ('nil', False, [(1L, u'dam'), (2L, u'sire')])
        results = MultipleAnimalsField().get_results(request, term='', page='1', context='')
        res = [(animal.id, animal.name) for animal in Animal.objects.all()]
        self.assertEqual(res, results[2])
        # result looks like this: ('nil', False, [(1L, u'dam')])
        results = MultipleAnimalsField().get_results(request, term='t', page='1', context='')
        self.assertEqual([(1L, u'tagie')], results[2])

    def test_sire_field(self):
        request = self.factory.get(reverse('django_select2_central_json'))
        # result looks like this: ('nil', False, [(4L, u'123', {})])
        results = BullField().get_results(request, term='s', page='1', context='')
        self.assertEqual((2L, u'sire', {}), results[2][0])