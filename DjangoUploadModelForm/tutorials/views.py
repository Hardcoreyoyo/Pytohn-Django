from django.shortcuts import render, redirect

from .forms import TutorialForm
from .models import Tutorial


def tutorialList(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/list.html', { 'tutorials' : tutorials})


def uploadTutorial(request):
    if request.method == 'POST':  
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tutorial_list')
    else:
        form = TutorialForm()
    return render(request, 'tutorial/upload.html', {'form' : form})


def deleteTutorial(request, pk):
    if request.method == 'POST':
        tutorial = Tutorial.objects.get(pk=pk)
        tutorial.delete()
    return redirect('tutorial_list')
