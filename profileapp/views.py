from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profiles_ownership_required
from profileapp.forms import ProfileCreateForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/create.html'
    # success_url = reverse_lazy('accounts:detail')

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(profiles_ownership_required, 'get')
@method_decorator(profiles_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreateForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'
    # success_url = reverse_lazy('accounts:hello_world')

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.user.pk})
