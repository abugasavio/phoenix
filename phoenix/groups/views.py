from django.shortcuts import redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.template.context import RequestContext
from smartmin.views import SmartCRUDL, SmartView, SmartCreateView, SmartReadView, SmartUpdateView, SmartListView
from phoenix.animals.views import AnimalCRUDL
from phoenix.health.views import TreatmentCRUDL
from phoenix.records.views import NoteCRUDL
from .models import Group
from .forms import GroupForm


class GroupNoteCRUDL(NoteCRUDL):

    class Create(NoteCRUDL.Create):

        def get(self, request, *args, **kwargs):
            group_id = request.GET.get('group', None)
            if group_id:
                try:
                    Group.objects.get(id=group_id)
                except Group.DoesNotExist:
                    messages.error(request, 'Group Id is required')
                    return redirect(request.META.get('HTTP_REFERER', reverse('groups.group_list')))
            else:
                messages.error(request, 'Group Id is required')
                return redirect(request.META.get('HTTP_REFERER', reverse('groups.group_list')))
            return super(NoteCRUDL.Create, self).get(request, *args, **kwargs)

        def post_save(self, obj):
            obj = super(NoteCRUDL.Create, self).post_save(obj)
            group_id = self.request.GET.get('group', None)
            obj.group = Group.objects.get(id=group_id)
            obj.save()
            return obj

        def get_success_url(self):
            return reverse('groups.group_read', args=[self.request.GET.get('group', None)])

    class List(NoteCRUDL.List):
        fields = ('id', 'date', 'file', 'details')

        def get_queryset(self, **kwargs):
            queryset = super(NoteCRUDL.List, self).get_queryset(**kwargs)
            queryset = queryset.filter(group=self.request.group)
            return queryset


class GroupTreatmentCRUDL(TreatmentCRUDL):

    class Create(TreatmentCRUDL.Create):
        fields = ('date', 'description', 'notes')

        def get(self, request, *args, **kwargs):
            group_id = request.GET.get('group', None)
            if group_id:
                try:
                    Group.objects.get(id=group_id)
                except Group.DoesNotExist:
                    messages.error(request, 'Group Id is required')
                    return redirect(request.META.get('HTTP_REFERER', reverse('groups.group_list')))
            else:
                messages.error(request, 'Group Id is required')
                return redirect(request.META.get('HTTP_REFERER', reverse('groups.group_list')))
            return super(GroupTreatmentCRUDL.Create, self).get(request, *args, **kwargs)

        def post_save(self, obj):
            obj = super(GroupTreatmentCRUDL.Create, self).post_save(obj)
            group_id = self.request.GET.get('group', None)
            group = Group.objects.get(id=group_id)
            obj.group = group
            obj.save()
            return obj

        def get_success_url(self):
            return reverse('groups.group_read', args=[self.request.GET.get('group', None)])

    class Update(TreatmentCRUDL.Update):
        fields = ('date', 'description', 'notes',)

        def get_success_url(self):
            animal_id = self.object.animals.all()[0].id
            return reverse('animals.animal_read', args=[animal_id])

    class List(TreatmentCRUDL.List):
        fields = ('id', 'type', 'date', 'description', 'notes')

        def get_queryset(self, **kwargs):
            queryset = super(GroupTreatmentCRUDL.List, self).get_queryset(**kwargs)
            queryset = queryset.filter(group=self.request.group)
            return queryset


class GroupCRUDL(SmartCRUDL):
    model = Group

    actions = ('create', 'read', 'update', 'list')

    class Create(SmartCreateView):
        form_class = GroupForm

    class Read(SmartReadView):
        fields = ('id', 'name', 'sex', 'breed', 'number_of_animals', 'start_birth_date', 'end_birth_date', 'created_on', 'created_by')

        def get_number_of_animals(self, obj):
            return obj.get_animals_queryset().count()

        def get_context_data(self, **kwargs):
            context_data = super(GroupCRUDL.Read, self).get_context_data(**kwargs)
            self.request.group = self.object

            animal_response = AnimalCRUDL().view_for_action('list').as_view()(self.request)
            if hasattr(animal_response, 'context_data'):
                context_data['animals'] = render_to_string('groups/animal_related_list.html', animal_response.context_data, RequestContext(self.request))

            treatment_response = GroupTreatmentCRUDL().view_for_action('list').as_view()(self.request)
            if hasattr(treatment_response, 'context_data'):
                treatment_response.context_data['add_url'] = reverse('groups.treatment_create') + '?group=' + str(self.request.group.id)
                context_data['treatment'] = render_to_string('health/treatment_related_list.html', treatment_response.context_data, RequestContext(self.request))

            note_response = GroupNoteCRUDL().view_for_action('list').as_view()(self.request)
            if hasattr(note_response, 'context_data'):
                note_response.context_data['add_url'] = reverse('groups.note_create') + '?group=' + str(self.request.group.id)
                context_data['notes'] = render_to_string('records/note_related_list.html', note_response.context_data, RequestContext(self.request))

            return context_data

    class Update(SmartUpdateView):
        form_class = GroupForm

    class List(SmartListView):
        fields = ('id', 'name', 'sex', 'breed', 'start_birth_date', 'end_birth_date')

