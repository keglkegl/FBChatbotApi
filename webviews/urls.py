from django.urls import path

from . import views

urlpatterns = [
    path('faq/nlb/list', views.nlb_faq_list, name='nlb_faq_list'),
]
