
from django.shortcuts import render
from .models import music

# Create your views here.
def Assignmentdemo(request):

    musics = music.objects.all() 
    
    return render(request, 'Assignmentdemo.html',{'musics': musics}) 
