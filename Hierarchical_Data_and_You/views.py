from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView

from Hierarchical_Data_and_You.forms import FileForm
from Hierarchical_Data_and_You.models import File


class LoginUserView(LoginView):
    template_name = 'generic-form.html'
    success_url = 'index.html'


@method_decorator(login_required, name='dispatch')
class LogoutUserView(LogoutView):
    next_page = '/'


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        files = File.objects.filter(user=self.request.user)
        context['files'] = files

        return context


@method_decorator(login_required, name='dispatch')
class CreateFileView(CreateView):
    template_name = 'generic-form.html'
    form_class = FileForm

    def form_valid(self, form):
        data = form.cleaned_data
        File.objects.create(
            user=data['user'],
            name=data['name'],
            parent=data['parent']
        )
        return HttpResponseRedirect(reverse_lazy('homepage'))
