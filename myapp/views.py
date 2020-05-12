from django.shortcuts import render
from myapp.forms import AddTextForm
from myapp.models import TextInput, TextOutpout
from subprocess import PIPE, run



def index(req):
    if req.method == "POST":
        form = AddTextForm(req.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            TextInput.objects.create(
                innerinput=data['textinput']
            )
            command = ['cowsay', data['textinput']]
            result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            cow = result.stdout
            form = AddTextForm()      
            return render(req, 'index.html', {'form': form, 'cow': cow })
    form = AddTextForm()
    return render(req, 'index.html', {'form': form})
       

    

def history(req):
    innertexts = TextInput.objects.filter().order_by('-id')[:10]
    return render(req, 'history.html', { "innertexts": innertexts })