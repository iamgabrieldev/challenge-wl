from django import generics, permissions
from django.views import TokenObtainPairView
from django import Response
from bank import serializers
from models import Wallet, Transaction
from serializers import WalletSerializer, TransactionSerializer, CreateTransactionSerializer

class WalletView(generics.RetrieveUpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.wallet

class CreateTransactionView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = CreateTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        sender_wallet = self.request.user.wallet
        recipient_wallet = serializer.validated_data['recipient'].wallet

        if sender_wallet.balance < serializer.validated_data['amount']:
            raise serializers.ValidationError("Saldo insuficiente.")

        sender_wallet.balance -= serializer.validated_data['amount']
        recipient_wallet.balance += serializer.validated_data['amount']
        sender_wallet.save()
        recipient_wallet.save()

        serializer.save(sender=self.request.user)