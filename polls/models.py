import datetime
from django.db import models
from django.utils import timezone

from django.contrib import admin


class Question(models.Model):
     # Stores the main poll question that users will see on the website.
    question_text = models.CharField(max_length=200)

     # Stores the date and time when the question was published.
     # This is used later to order questions and check if they were published recently
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        # Makes Question objects display as readable text in the admin page and Django shell.
        return self.question_text
   
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        # Returns True if the question was published within the last 24 hours.
        # This is used in the admin list display to quickly identify recent questions. 
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    # Connects each answer choice to one specific Question.
    # If a Question is deleted, all of its related Choices are deleted as well.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

     # Stores the text for each possible answer choice.
    choice_text = models.CharField(max_length=200)

     # Tracks how many votes this choice has received.
    # The default value is 0 because a new choice starts with no votes.
    votes = models.IntegerField(default=0)

    def __str__(self):
        # Makes Choice objects display as readable text in the admin page and Django shell.
        return self.choice_text
    


   