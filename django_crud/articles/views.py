from django.shortcuts import render

# Create your views here.
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    return render(request, 'articles/create.html')