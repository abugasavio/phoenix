from django.db import models
from smartmin.models import SmartModel
from phoenix.animals.models import Animal


class Group(SmartModel):
    name = models.CharField(max_length=30)
    sex = models.CharField(choices=Animal.SEX_CHOICES, max_length=20)
    breed = models.ForeignKey('animals.Breed', null=True, blank=True)
    start_birth_date = models.DateField(null=True, blank=True)
    end_birth_date = models.DateField(null=True, blank=True)
    sire = models.ForeignKey('animals.Animal', null=True, blank=True, related_name='sire_groups')
    dam = models.ForeignKey('animals.Animal', null=True, blank=True, related_name='dam_groups')

    def __unicode__(self):
        return self.name

    def get_animals_queryset(self):
        queryset = Animal.objects.all()
        if self.sex:
            queryset = queryset.filter(sex=self.sex)
        if self.breed:
            queryset = queryset.filter(breed=self.breed)
        if self.start_birth_date:
            queryset = queryset.filter(birth_date__gte=self.start_birth_date)
        if self.end_birth_date:
            queryset = queryset.filter(birth_date__lte=self.start_birth_date)
        if self.sire:
            queryset = queryset.filter(sire=self.sire)
        if self.dam:
            queryset = queryset.filter(dam=self.dam)

        return queryset