from django.urls import path
from .views import TypeListCreateView, TypeRetrieveUpdateDestroyView

urlpatterns = [
    path('', TypeListCreateView.as_view(), name='type-list-create'),
    path('<slug:slug>/', TypeRetrieveUpdateDestroyView.as_view(), name='type-detail'),
]
