from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("", views.index, name=""),
    path("helloAccounts/", views.index, name="helloAccounts"),
    path("addFive/<int:accountID>", views.addFive, name ="addFive")
]