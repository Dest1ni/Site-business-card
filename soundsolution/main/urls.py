from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('main-page/',views.MainPage.as_view(),name='main-page'),
    path('contacts/',views.ContactPage.as_view(),name='contacts'),
    path('about/',views.AboutPage.as_view(),name='about'),
]