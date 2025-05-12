from django.shortcuts import render
from .models import Talaba

def index(request):
    talabalar = Talaba.objects.all()
    return render(request, 'index.html', {'talabalar': talabalar})

