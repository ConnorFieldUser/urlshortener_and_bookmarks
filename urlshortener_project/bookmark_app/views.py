from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from bookmark_app.models import Bookmark

# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class IndexView(TemplateView):
        template_name = 'index.html'


class BookmarkSim(TemplateView):
        template_name = 'sim_create_bookmark.html'


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ('title', 'description', 'url', 'newrl', 'private')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)
