from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreateForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/create.html'
    success_url = reverse_lazy('accounts:hello_world')

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)
