from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice

# Index view
def index(request):
    latest_question_list = Question.objects.all()
    context = {
        "latest_question_list": latest_question_list
    }
    return render (request, "polls/index.html", context)

# Detail view
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context ={"question": question}

    return render (request, "polls/detail.html", context)

# Result view
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context ={"question": question}

    return render (request, "polls/results.html", context)

# Vote view
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    selected_choice = request.POST["choice"]
    choice = Choice.objects.get(pk=selected_choice)
    choice.votes += 1
    choice.save()

    return redirect("results", question_id=question.id)