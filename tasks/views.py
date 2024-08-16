import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
# Create your views here.
from .models import Task


@login_required
def taskList(request):
  search = request.GET.get('search')
  filter = request.GET.get('filter')

  #contadores do dashboard
  tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now() - datetime.timedelta(days=30), user=request.user).count()
  tasksDone = Task.objects.filter(done='done', user=request.user).count()
  tasksDoing = Task.objects.filter(done='doing', user=request.user).count()
  
  if search:
    tasks = Task.objects.filter(title__icontains=search, user=request.user) # adicionamos user para filtrar por user autenticado.
  
  elif filter:
    tasks = Task.objects.filter(done=filter, user=request.user)
  
  else:
    tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user) # aqui traz tudo do usuário autenticado.
    paginator = Paginator(tasks_list, 2) # mostra 2 tarefas por vez

    page = request.GET.get('page')  # pega o numero da pagina

    tasks = paginator.get_page(page)  # pega a pagina
    
  return render(request, 'tasks/list.html', {
    'tasks': tasks,
    'tasksrecently': tasksDoneRecently, 
    'tasksdone': tasksDone, 
    'tasksdoing': tasksDoing
  })	

@login_required
def taskView(request, id):
  task = get_object_or_404(Task, pk=id, user=request.user)
  print({request.user})
  return render(request, 'tasks/task.html', {'task': task})

@login_required
def newTask(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)

    if form.is_valid():
      task = form.save(commit=False) # commit=False faz para o evento padrão de salvar
      # para podermos mudar o estado de tarefa de done defalt doing
      task.done = 'doing' # adicionando
      task.user = request.user # adicionando o id do usuário autenticado
      task.save() # salvando normalmente
      return redirect('/') # feito isso vamos redirecionar para lista de tarefas
  else:
    form = TaskForm()
    return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def editTask(request, id):
  task = get_object_or_404(Task, pk=id, user=request.user)
  form = TaskForm(instance=task) # para deixa o formulário pré populado para editar usamos instance True.

  if(request.method == 'POST'):	
    form = TaskForm(request.POST, instance=task)
    
    if(form.is_valid()):
      task.save()
      return redirect('/')
    else:
      return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

  else:
    return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

@login_required
def deleteTask(request, id):
  task = get_object_or_404(Task, pk=id, user=request.user)
  task.delete()

  messages.info(request, 'Tarefa deletada com sucesso.')

  return redirect('/')

@login_required
def changeStatus(request, id):
  task = get_object_or_404(Task, pk=id, user=request.user)

  if task.done == 'doing':
    task.done = 'done'
  else:
    task.done = 'doing'

  task.save()

  if request.GET.get('page'):
    return redirect(f'/?page={request.GET.get("page")}')
  elif request.GET.get('search'):
    return redirect(f'/?search={request.GET.get("search")}')
  else:
    return redirect('/')

# def helloworld(request):
#   return HttpResponse('Hello World!')	

# def yourName(request, name):
#   return render(request, 'tasks/yourname.html', {'name': name})

