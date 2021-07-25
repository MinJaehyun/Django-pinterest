from django.shortcuts import render
from accounts.models import HelloWorld


def hello_world(request):
    # post
    if request.method == "POST":
        temp = request.POST.get('hello_input')
        hello_world = HelloWorld()
        hello_world.text = temp
        hello_world.save()

        return render(request, 'accounts/hello_world.html', context={"hello_world_output": hello_world})

    # get
    else:
        return render(request, 'accounts/hello_world.html', context={"hello_world_output": "GET METHOD"})
