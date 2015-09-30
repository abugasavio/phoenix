# -*- coding: utf-8 -*-
from django.conf.urls import patterns

from . import views

urlpatterns = patterns('',
)

urlpatterns.extend(views.GroupCRUDL().as_urlpatterns())
urlpatterns.extend(views.GroupTreatmentCRUDL().as_urlpatterns())
urlpatterns.extend(views.GroupNoteCRUDL().as_urlpatterns())