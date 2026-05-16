from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegisterForm, TaskForm
from .models import Task

# register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

# dashboard
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')

    else:
        form = TaskForm()

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'form': form
    })

# complete task
@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('dashboard')

# delete task
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('dashboard')

# admin only page
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    tasks = Task.objects.all()
    return render(request, 'admin.html', {'tasks': tasks})