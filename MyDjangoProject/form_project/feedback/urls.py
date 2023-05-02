from django.contrib import admin
from django.urls import path
from .views import index, done, update_feedback, FeedbackView, FeedBackUpdateView, DoneView, ListFeedBack, DetailFeedBack, FeedbackViewUpdate

urlpatterns = [
    path("", FeedbackView.as_view()),
    path("done", DoneView.as_view()),
    path("<int:id_feedback>", FeedBackUpdateView.as_view()),
    path("list", ListFeedBack.as_view()),
    path("detail/<int:pk>", DetailFeedBack.as_view()),
    path("update/<int:pk>", FeedbackViewUpdate.as_view()),
]

