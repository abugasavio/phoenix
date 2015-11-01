# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',)

urlpatterns.extend(views.AnimalCRUDL().as_urlpatterns())
urlpatterns.extend(views.ServiceCRUDL().as_urlpatterns())
urlpatterns.extend(views.PregnancyCheckCRUDL().as_urlpatterns())
urlpatterns.extend(views.AnimalMilkProductionCRUDL().as_urlpatterns())
urlpatterns.extend(views.MilkProductionCRUDL().as_urlpatterns())
urlpatterns.extend(views.AnimalTreatmentCRUDL().as_urlpatterns())
urlpatterns.extend(views.BreedCRUDL().as_urlpatterns())
urlpatterns.extend(views.ColorCRUDL().as_urlpatterns())
urlpatterns.extend(views.AnimalNoteCRUDL().as_urlpatterns())
urlpatterns.extend(views.SireCRUDL().as_urlpatterns())
urlpatterns.extend(views.DamCRUDL().as_urlpatterns())
urlpatterns.extend(views.BreederCRUDL().as_urlpatterns())

