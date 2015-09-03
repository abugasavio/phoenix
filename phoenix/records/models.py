from django.db import models
from smartmin.models import SmartModel


class Note(SmartModel):
    group = models.ForeignKey('groups.Group', null=True, blank=False)
    animals = models.ManyToManyField('animals.Animal', null=False, blank=False, related_name='notes')
    date = models.DateField(null=True, blank=True)
    file = models.FileField(max_length=100, upload_to='notes', null=True, blank=True)
    details = models.TextField(blank=True)


class AnimalDocument(models.Model):
    file = models.FileField(upload_to='documents', max_length=255)
    animal = models.ForeignKey('animals.Animal', related_name='documents')
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return u"Document of '%s'" % self.animal

    def delete(self):
        self.deleted = True
        self.save()
