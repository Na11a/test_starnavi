from django.urls import path 
from .views import HomeListView, PostCreateView,PostDeleteView,PostUpdateView
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

urlpatterns = [
    path('edit-page/',PostCreateView.as_view(), name = 'edit_page'),
    path('update-page/<int:pk>',PostUpdateView.as_view(), name = 'update_page'),
    path('delete-page/<int:pk>',PostDeleteView.as_view(), name = 'delete_page'),
  
]

    