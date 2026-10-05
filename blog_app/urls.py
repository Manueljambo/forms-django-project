from django.urls import path
from .views import(
       HomePageView,
       BlogDetailView,
       BlogCreateView,
       BlogEditView,
       BlogDeleteView  
) 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('Post/<int:pk>/', BlogDetailView.as_view(), name='post-details'),
    path('/post_new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete-post')
]