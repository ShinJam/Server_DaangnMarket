from django.urls import path

from post.views import (
    PostListAPI,
    PostLikeSave,
    PostDetailAPI,
    PostCreateAPI,
    PostImageUploadAPI,
    SearchAPI,
    SearchSaveAPI,
    PostLikeList
)

app_name = 'post'
urlpatterns = [
    path('list/', PostListAPI.as_view()),
    path('detail/', PostDetailAPI.as_view()),
    path('create/', PostCreateAPI.as_view()),
    path('image/upload/', PostImageUploadAPI.as_view()),
    # TODO : viewset 으로 분리
    path('search/', SearchAPI.as_view()),
    path('search/save/', SearchSaveAPI.as_view()),
  
    # TODO :
    path('like/', PostLikeSave.as_view()),
    path('like/list/', PostLikeList.as_view()),
]
