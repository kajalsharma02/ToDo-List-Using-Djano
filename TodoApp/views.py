from django.shortcuts import render, HttpResponse
from TodoApp.models import Task

# from django.shortcuts import redirect, get_object_or_404


# Create your views here.
def home(request):
    context = {'success' : False}
    if request.method == 'POST':
        title = request.POST['task']
        des = request.POST['des']
        print(title, des)
        final = Task(tasks = title, description = des)
        final.save()
        context = {'success' : True}

    return render(request, 'index.html', context)

def task(request):
    allTask = Task.objects.all()
    print(allTask)
    for i in allTask:
        print(i.tasks, i.description)  
    context = {'data' : allTask}
    return render(request, 'task.html',context)

# def delete_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('task')