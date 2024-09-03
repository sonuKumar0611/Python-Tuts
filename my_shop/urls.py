from django.urls import path
from . import views

urlpatterns=[
    path('', views.show_my_shop , name="my_shop"),
]