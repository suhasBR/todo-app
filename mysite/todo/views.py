from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import xlwt

from .models import Task
import csv


def index(request):

    tasks = Task.objects.all()
    context = {
        'task_list' : tasks,
    }
    return render(request,'todo/index.html',context)

def add_task(request):
    t = Task(task_name=request.POST['task'],description=request.POST['description'])
    t.save()
    # return HttpResponse("done")
    return HttpResponseRedirect(reverse('todo:index'))

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)

    tasks = Task.objects.all().values_list('task_name','description')
    for task in tasks:
        # writer.writerow([task.task_name])
        writer.writerow(task)

    # users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    # for user in users:
    #     writer.writerow(user)

    return response
    return HttpResponseRedirect(reverse('todo:index'))

def export_users_xlsx(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tasks')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Task', 'Description']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Task.objects.all().values_list('task_name','description')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
    return HttpResponseRedirect(reverse('todo:index'))

def delete_task(request):
    t=Task.objects.filter(task_name=request.POST['task_name'])
    t.delete()
    return HttpResponseRedirect(reverse('todo:index'))








# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
# def detail(request,question_id):
#
#     question = get_object_or_404(Question,pk = question_id)
#     return render(request,'polls/detail.html',{'question':question})
