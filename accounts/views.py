from django.shortcuts import render

def hello_world(request):
    return render(request, 'accounts/hello_world.html')
