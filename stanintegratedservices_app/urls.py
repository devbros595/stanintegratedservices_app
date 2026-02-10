from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact-us/', views.contact_view, name='contact'),
    path('services/', views.services_view, name='services'),
    path('why-choose-us/', views.why_choose_us_view, name='why_choose_us'),
]