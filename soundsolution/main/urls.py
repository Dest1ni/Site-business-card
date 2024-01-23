from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.MainPage.as_view(),name='main-page'),
    #path('bithday/',views.BirthdayPage.as_view(),name='birthday-page'),
]