from django.urls import path,include
from  .views import *

urlpatterns = [
    path('home/',home_view ,name='home'),
    path('post/create/',post_create_view,name='post-create')
]