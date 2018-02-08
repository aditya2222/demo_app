from django.urls import path
from blog.views import *
urlpatterns=[
    path('posts',PostListView.as_view(),name='post_list'),
    path('',AboutView.as_view(),name='about'),
    path('post/<int:pk>/details',PostDetailView.as_view(),name='post_detail'),
    path('post/new/',CreatePost.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',UpdatePostView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/',PostDeleteView.as_view(),name='post_delete'),
    path('drafts/',DraftListView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/publish',post_publish,name='post_publish'),

]