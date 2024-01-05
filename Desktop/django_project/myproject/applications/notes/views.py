from django.shortcuts import render

# if we will enter a wrong pk key then it will throw some exception so for handle that error we have to import
from django.http import Http404
# Create your views here.
from .models import Notes

def list(request):
    all_notes= Notes.objects.all()
    return render(request,'notes/notes_list.html',{'notes':all_notes})


def detail(request,pk):
    #  for handling wrong pk key we have to add try cactch
    try:
        note= Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")    
    return render(request,'notes/notes_detail.html',{'note': note})