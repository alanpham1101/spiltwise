from django.shortcuts import render

from rest_framework.views import APIView


class GetUsersList(APIView):
    def get(self, request, **kwargs):
        pass


class AddExpense(APIView):
    def post(self, request, **kwargs):
        pass


class SettleUp(APIView):
    def post(self, request, **kwargs):
        pass
