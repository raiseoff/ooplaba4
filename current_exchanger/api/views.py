from rest_framework.views import APIView
from rest_framework.response import Response
from currency.models import Currency
from .serializers import CurrencySerializer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CurrencyExchange(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        currencyFrom = request.data['currencyFrom']
        currencyTo = request.data['currencyTo']
        ammount = request.data['ammount']
        try:
            ammount = float(ammount)
        except:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        if ammount <= 0:
            return Response("Amount should be more than zero", status=status.HTTP_400_BAD_REQUEST)
        if not(Currency.objects.filter(CharCode=currencyFrom).exists() and Currency.objects.filter(CharCode=currencyTo).exists() and (type(ammount) in [int, float])):
            return Response("Invalid data2", status=status.HTTP_400_BAD_REQUEST)
        currencyFrom = Currency.objects.filter(CharCode=currencyFrom).first()
        currencyTo = Currency.objects.filter(CharCode=currencyTo).first()
        result = currencyFrom.exchange_to(ammount, currencyTo)
        return Response(f"{result}", status=status.HTTP_200_OK)
# {
#     "currencyFrom": "USD",
#     "currencyTo": "RUB",
#     "ammount": 1
# }