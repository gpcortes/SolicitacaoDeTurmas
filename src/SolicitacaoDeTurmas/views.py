from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .forms import SolicitacaoDeTurmas

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SolicitacaoDeTurmas(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    elif request.method == 'GET':
        form = SolicitacaoDeTurmas()

    return render(request, 'form.html', {'form': form})

def processa_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SolicitacaoDeTurmas(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
    elif request.method == 'GET':
        return HttpResponseRedirect('/form/')
    return HttpResponse(form)
