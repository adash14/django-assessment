from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    # Allows choices to be edited directly inside the Question admin page.
    # TabularInline displays choices in a compact table format.
    model = Choice

     # Shows three blank choice fields when creating a new question.
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # Organizes the Question form into labeled sections in the admin page.
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    # Adds related Choice objects directly below the Question fields.
    inlines = [ChoiceInline]

     # Controls which columns appear on the Question list page.
    list_display = ["question_text", "pub_date", "was_published_recently"]

     # Adds a sidebar filter so admins can filter questions by publication date.
    list_filter = ["pub_date"]

    # Adds a search box so admins can search questions by question text.
    search_fields = ["question_text"]

# Registers the Question model with the customized admin settings above.
admin.site.register(Question, QuestionAdmin)

