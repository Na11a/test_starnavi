from django.contrib import admin
from django.urls import path, include
from user.views import LoginView, RegisterUserView,Logout
from post.views import HomeListView,like_unlike_post
from django.conf.urls import url

    
urlpatterns = [
    path('api/analitics/',include('post.api.urls')),
    path('liked/', like_unlike_post, name='like-post-view'),
    path('',HomeListView.as_view(),name = 'home'),
    path('admin/', admin.site.urls),
    path('posts/',include('post.urls')),
    path('login/',LoginView.as_view(), name= 'login_page'),
    path('registration/',RegisterUserView.as_view(), name= 'registration_page'),
    path('logout/',Logout.as_view(),name='logout'),
]

