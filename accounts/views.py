from django.shortcuts import render


def hello_world(request):
    # post
    if request.method == "POST":
        return render(request, 'accounts/hello_world.html', context={"text": "POST METHOD"})

    # get
    else:
        return render(request, 'accounts/hello_world.html', context={"text": "GET METHOD"})
