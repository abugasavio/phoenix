from django.conf.urls import patterns

from . import views

urlpatterns = patterns('',
)

urlpatterns.extend(views.TreatmentCRUDL().as_urlpatterns())