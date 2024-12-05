from django.urls import path,include
from  .views import *

urlpatterns = [
    path('',home_view ,name='home'),
    path('post/create/',post_create_view,name='post-create'),
    path('post/delete/<pk>/',post_delete_view,name='post-delete'),
    path('post/edit/<pk>/',post_edit_view,name='post-edit'),
    path('post/view/<pk>/',post_page_view,name='post-view'),
    path('post/like/<pk>/',like_post,name='like-post'),
    path('post/category/<tag>/',home_view,name='post-category-view'),
    path('post/comment/sent/<pk>/',comment_sent,name='post-comment-sent'),
    path('post/comment/delete/<pk>/',comment_delete_view,name='post-comment-delete'),
    path('post/comment/reply/sent/<pk>/',reply_sent,name='comment-reply-sent'),
    path('post/comment/reply/delete/<pk>/',reply_delete_view,name='comment-reply-delete'),
]