from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import AccountUpdateForm
from accounts.models import HelloWorld


def hello_world(request):
    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

class AccountsCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/create.html'
    success_url = reverse_lazy('accounts:hello_world')


class AccountsDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accounts/detail.html'


class AccountsUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('accounts:detail')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().post(*args,**kwargs)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))


class AccountsDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('accounts:login')
