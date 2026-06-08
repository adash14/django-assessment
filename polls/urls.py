from django.urls import path

from . import views

# App namespace used by templates, such as {% url 'polls:detail' question.id %}.
# This helps avoid hardcoding URLs in HTML files.
app_name = "polls"

urlpatterns = [
     # Polls homepage: shows the five latest questions.
    path("", views.IndexView.as_view(), name="index"),

     # Detail page: shows one question and its answer choices.
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

     # Results page: shows the vote totals for one question.
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # Vote route: handles the POST request when a user submits a vote.
    path("<int:question_id>/vote/", views.vote, name="vote"),
]