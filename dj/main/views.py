from  django.http import HttpResponseRedirect
from  django.urls import reverse
from django.shortcuts import render
from django import forms
# Create your views here.

tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Add Task:")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "main/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request, "main/add.html", {
                "form": form
            })

    return render(request, "main/add.html", {
        "form": NewTaskForm()
    })