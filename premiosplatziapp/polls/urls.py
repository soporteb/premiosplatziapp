from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    #es; /polls/
    path("", views.IndexView.as_view(), name="index"),
    #es; /polls/5/
    path("<int:pk>/detail/", views.DetailView.as_view(), name="detail"),
    #es; /polls/5/results/
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    #es; /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]