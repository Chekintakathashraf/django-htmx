from django.urls import path,include
from  .views import *

urlpatterns = [
    path('',home_view ,name='home'),
    path('post/create/',post_create_view,name='post-create'),
    path('post/delete/<pk>/',post_delete_view,name='post-delete'),
    path('post/edit/<pk>/',post_edit_view,name='post-edit'),
    path('post/view/<pk>/',post_page_view,name='post-view'),
    path('post/category/<tag>/',home_view,name='post-category-view'),
]