from django.urls import path
from savedposts import views

urlpatterns = [
    path('savedposts/', views.SavedPostList.as_view()),
    path('savedposts/<int:pk>/', views.SavedPostDetail.as_view()),
]