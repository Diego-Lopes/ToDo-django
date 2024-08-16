from django import forms

from .models import Task

# usamos o forms do django para tratar as informações que está na model
# e tambem usamos algumas segurança de uso e validação.

class TaskForm(forms.ModelForm):
  class Meta: # faz o class Meta do forms nele definimos o model que é o Task
    # depois os fields podemos escolher o que vai ser exibido no formulário.
    model = Task
    fields = ['title', 'description']