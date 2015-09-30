from datetime import date
from django.test import TestCase
from django.contrib.auth.models import Permission
from model_mommy import mommy
from phoenix.utils.test_utils import create_logged_in_user
from phoenix.animals.models import Animal
from phoenix.finances.models import Transaction


class TransactionTestCae(TestCase):

    def setUp(self):
        self.laryn = mommy.make('animals.Animal', ear_tag='432', sex=Animal.SEX_CHOICES.female)
        self.shauna = mommy.make('animals.Animal', ear_tag='302', sex=Animal.SEX_CHOICES.female)
        self.income = mommy.make('finances.Transaction', date=date.today(), amount=2000, transaction_type=Transaction.types.income)
        self.income.animals.add(self.shauna, self.laryn)
        self.expense = mommy.make('finances.Transaction', date=date.today(), amount=2000, transaction_type=Transaction.types.expense)
        self.expense.animals.add(self.shauna, self.laryn)

    def test_creating_transaction(self):
        user = create_logged_in_user(self)
        user.user_permissions.add(Permission.objects.get(codename='transaction_create'))
        user.user_permissions.add(Permission.objects.get(codename='transaction_list'))

        post_data = {
            'date': date.today(),
            'animals': [self.shauna.id, self.laryn.id],
            'amount': 3000
        }
        #url = reverse('finances.transaction_create') + '?type=income'
        #response = self.client.post(url, post_data, follow=True)
        #self.assertContains(response, 'Your new transaction has been created')
