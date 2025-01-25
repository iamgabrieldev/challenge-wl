from django.test import TestCase
from django import status
from django.test import APIClient
from .models import User, Wallet, Transaction

class TransactionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)

    def test_create_transaction(self):
        recipient = User.objects.create_user(username='recipient', password='password')
        data = {'recipient': recipient.id, 'amount': 100}
        response = self.client.post('/transactions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)

class IntegrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_complete_transaction_flow(self):
        user1 = User.objects.create_user(username='user1', password='password')
        user2 = User.objects.create_user(username='user2', password='password')

        self.client.force_authenticate(user=user1)

        data = {'amount': 1000}
        response = self.client.put('/wallets/me/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'recipient': user2.id, 'amount': 500}
        response = self.client.post('/transactions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user1_wallet = Wallet.objects.get(user=user1)
        user2_wallet = Wallet.objects.get(user=user2)
        self.assertEqual(user1_wallet.balance, 500)
        self.assertEqual(user2_wallet.balance, 500)