from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth.forms import UserCreationForm


from accounts.forms import UpdateForm, ProfileForm, SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserProfileView(LoginRequiredMixin, TemplateView):
    form_class = ProfileForm
    template_name = 'registration/profile.html'

    def get_queryset(self):
        return User.objects.get(id=self.request.user.id)


class UpdateView(LoginRequiredMixin, FormView):
    template_name = 'registration/change.html'
    form_class = UpdateForm
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        # formのupdateメソッドにログインユーザーを渡して更新
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # 更新前のユーザー情報をkwargsとして渡す
        kwargs.update({
            'email': self.request.user.email,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'age': self.request.user.age,
        })
        return kwargs
