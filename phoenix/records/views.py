from smartmin.views import SmartCRUDL, SmartCreateView, SmartReadView, SmartListView, SmartUpdateView
from phoenix.utils.upload.views import UploadView, UploadListView, UploadDeleteView
from .models import Note, AnimalDocument
from .forms import NoteForm


class AnimalDocumentUploadView(UploadView):
    model = AnimalDocument
    fields = ('file', 'animal')
    delete_url = 'records.animaldocument_delete'

    def get_context_data(self, **kwargs):
        context = super(AnimalDocumentUploadView, self).get_context_data(**kwargs)
        context['animal'] = self.request.animal
        return context


class AnimalDocumentListView(UploadListView):
    model = AnimalDocument
    delete_url = 'records.animaldocument_delete'

    def get_queryset(self):
        return AnimalDocument.objects.filter(animal=self.kwargs['pk']).filter(deleted=False)


class AnimalDocumentDeleteView(UploadDeleteView):
    model = AnimalDocument


class NoteCRUDL(SmartCRUDL):
    model = Note

    class Create(SmartCreateView):
        fields = ('date', 'file', 'details')

        form_class = NoteForm

    class Read(SmartReadView):
        fields = ('id', 'date', 'file', 'details', 'created', 'modified')

        def get_file(self, obj):
            return '<a href=' + obj.file.url + '>' + obj.file.name + '</a>'

    class List(SmartListView):
        fields = ('id', 'date', 'file', 'details')

        def get_file(self, obj):
            if obj.file:
                return '<a href=' + obj.file.url + '>' + obj.file.name + '</a>'
            return ''

    class Update(SmartUpdateView):
        fields = ('date', 'description', 'notes')
        form_class = NoteForm
