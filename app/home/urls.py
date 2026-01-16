from django.urls import path
from django.views.generic import RedirectView
from views.home_view import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('', RedirectView.as_view(url='home/', permanent=False)),
]
