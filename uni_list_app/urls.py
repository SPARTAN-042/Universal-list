from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    # path('uni_list_app/', views.uni_list_app, name='uni_list_app'),
    # path('uni_list_app/details/<int:id>', views.details, name='details'),
    # path('uni_list_app/')
]
