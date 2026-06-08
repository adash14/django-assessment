from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone 

from .models import Choice, Question


class IndexView(generic.ListView):
     # Uses the existing index.html template instead of Django's default question_list.html.
    template_name = "polls/index.html"

    # Renames the default object list so the template can use latest_question_list.
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
     # Returns the five most recent poll questions, ordered by publication date.
        # The minus sign before pub_date means newest questions appear first.


class DetailView(generic.DetailView):
    # Displays one specific Question and its answer choices.
    model = Question

     # Uses the custom detail template instead of Django's default question_detail.html.
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    # Displays voting results for one specific Question.
    model = Question

     # Uses a separate results template so the results page can look different from the detail page.
    template_name = "polls/results.html"
    

def vote(request, question_id):
     # Finds the Question being voted on.
    # If the question does not exist, Django automatically returns a 404 error page.
    question = get_object_or_404(Question, pk=question_id)

    try:
         # Gets the selected choice from the submitted POST form data.
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        # If the user submits the form without choosing an answer,
        # reload the detail page with an error message.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
         # Increases the selected choice's vote count by 1.
        # F("votes") + 1 lets the database handle the update safely.
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    








