from django.urls import path
from commentreactions import views

urlpatterns = [
    path('commentreactions/', views.CommentReactionList.as_view()),
    path('commentreactions/<int:pk>/', views.CommentReactionDetail.as_view()),
]
