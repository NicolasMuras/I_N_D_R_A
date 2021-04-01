from django.shortcuts import render
from main.forms import UsuarioForm

def schedule_view(request):

    if request.method == 'POST':

        form = PersonaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')
    else:
        form = UsuarioForm()
        context = {
            'form':form,
        }
        
    return render(request, 'index.html', {'form':form})
