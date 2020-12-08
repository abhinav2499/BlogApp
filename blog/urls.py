from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('blog/', PostList.as_view()),
    path('blog/<int:pk>/', PostDetail.as_view())
]
