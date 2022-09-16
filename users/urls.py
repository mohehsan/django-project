from django.urls import path

from .views import show_profile
from . import views

urlpatterns = [
    path('<int:pk>', views.show_profile, name='show_profile'),
    path('edit/<int:pk>', views.edit_profile, name='edit_profile'),
]
