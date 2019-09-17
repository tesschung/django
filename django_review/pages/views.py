from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def greeting(request, name):
    context = {'name': name}
    return render(request, 'pages/greeting.html', context)
