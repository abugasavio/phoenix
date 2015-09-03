from django.db import models
from smartmin.models import SmartModel


class Treatment(SmartModel):
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    group = models.ForeignKey('groups.Group', null=True, blank=False)
    animals = models.ManyToManyField('animals.Animal', null=False, blank=False, related_name='treatments')