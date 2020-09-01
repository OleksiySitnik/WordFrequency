from django.urls import path
from . import views

urlpatterns = [
    path('', views.TextList.as_view(), name='text-list'),
    path('create/', views.TextCreate.as_view(), name='text-create'),
    path('<int:pk>/', views.TextDetail.as_view(), name='text-details')
]