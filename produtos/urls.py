from django.urls import path
from . import views

urlpatterns = [
    path('pesquisa/', views.pesquisa_produto, name='pesquisa_produto'),
]
