from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accounts.models import HelloWorld


def hello_world(request):
    # post
    if request.method == "POST":
        temp = request.POST.get('hello_input')
        hello_world = HelloWorld()
        hello_world.text = temp
        hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accounts:hello_world'))

    # get
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accounts/hello_world.html', context={"hello_world_list": hello_world_list})
