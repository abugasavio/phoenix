from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import redirect
from smartmin.views import SmartCRUDL, SmartCreateView, SmartUpdateView, SmartListView
from phoenix.utils.view_utils import AjaxTemplateMixin
from .models import Transaction, Category
from .forms import TransactionForm, CategoryForm


class CategoryFormView(AjaxTemplateMixin, CreateView):
    ajax_template_name = 'finances/category_create_inner.html'
    form_class = CategoryForm

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')

    def form_valid(self, form):
        if hasattr(form.instance, 'created_by_id') and self.request.user.id >= 0:
            form.instance.created_by = self.request.user

        # auto populate modified_by if it is present
        if hasattr(form.instance, 'modified_by_id') and self.request.user.id >= 0:
            form.instance.modified_by = self.request.user

        return super(CategoryFormView, self).form_valid(form)


class CategoryCRUDL(SmartCRUDL):
    model = Category

    class Create(SmartCreateView, AjaxTemplateMixin):

        def get_success_url(self):
            animal_id = self.request.session.get('animal_id', None)
            return reverse('finances.transaction_create') + '?animal=' + animal_id


class TransactionCRUDL(SmartCRUDL):
    model = Transaction

    class Create(SmartCreateView):
        form_class = TransactionForm
        fields = ('date', 'category', 'animals', 'amount', )

        def get(self, request, *args, **kwargs):
            transaction_type = request.GET.get('type', None)
            transaction_types = Transaction.types
            if not transaction_type or transaction_type not in transaction_types:
                messages.warning(request, 'Transaction type is missing or is not valid')
                return redirect(request.META.get('HTTP_REFERER', '/'))
            return super(TransactionCRUDL.Create, self).get(request, *args, **kwargs)

        def pre_save(self, obj):
            obj.transaction_type = self.request.GET.get('type', None)
            return obj

    class Update(SmartUpdateView):
        form_class = TransactionForm
        fields = ('date', 'category', 'animals', 'amount', )

        def customize_form_field(self, name, field):
            field = super(TransactionCRUDL.Update, self).customize_form_field(name, field)
            if name == 'animals':
                # Force the minimumInputLength to 0, so that it shows all the contacts by default
                transaction = self.get_object()
                animals = transaction.animals
                field.widget.options['minimumInputLength'] = 0
                field.widget.choices = [(animal.id, str(animal)) for animal in animals.order_by('name').all()]
                field.initial = [animal.id for animal in animals.order_by('name').all()]
            return field

    class List(SmartListView):
        fields = ('id', 'date', 'transaction_type', 'category', 'amount', )
        field_config = {
            'transaction_type': (dict(label='Type')),
        }

        def get_transaction_type(self, obj):
            return obj.transaction_type.capitalize()

        def get_category(self, obj):
            return obj.category if obj.category else ''
