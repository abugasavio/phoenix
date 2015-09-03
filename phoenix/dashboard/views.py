from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from braces.views import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get(self, *args, **kwargs):
        return render_to_response(self.template_name, {}, context_instance=RequestContext(self.request))

    def get_context_data(self, **kwargs):
        context_data = super(DashboardView, self).get_context_data(**kwargs)
        context_data['number_livestock'] = None

        return context_data
