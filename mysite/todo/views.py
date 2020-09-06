from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Task
import csv


def index(request):

    tasks = Task.objects.all()
    context = {
        'task_list' : tasks,
    }
    return render(request,'todo/index.html',context)

def add_task(request):
    t = Task(task_name=request.POST['task'])
    t.save()
    # return HttpResponse("done")
    return HttpResponseRedirect(reverse('todo:index'))

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)

    tasks = Task.objects.all()
    for task in tasks:
        writer.writerow([task.task_name])

    # users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    # for user in users:
    #     writer.writerow(user)

    return response
    return HttpResponseRedirect(reverse('todo:index'))




# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
# def detail(request,question_id):
#
#     question = get_object_or_404(Question,pk = question_id)
#     return render(request,'polls/detail.html',{'question':question})
