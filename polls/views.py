from django.shortcuts import get_object_or_404, render
<<<<<<< refs/remotes/origin/part4
=======
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
>>>>>>> local

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

<<<<<<< refs/remotes/origin/part4
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
=======
>>>>>>> local

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

<<<<<<< refs/remotes/origin/part4
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
=======
>>>>>>> local

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't selected a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
