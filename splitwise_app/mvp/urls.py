from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.GetUsersList, name='get_users_list'),
    path('add_expense/', views.AddExpense, name='add_expense'),
    path('settle_up/', views.SettleUp, name='settle_up'),
]
