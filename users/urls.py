from django.urls import path,include
from  .views import *

urlpatterns = [
    path('profile/',profile_view ,name='profile'),
    path('profile/edit/',profile_edit_view ,name='profile-edit'),
]