from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from bookmark_app.models import Bookmark, Profile

import string
from random import shuffle

# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class IndexView(TemplateView):
        template_name = 'index.html'


class BookmarkCreateView(CreateView):
    model = Bookmark
    success_url = "/"
    fields = ('title', 'description', 'url', 'newrl', 'private')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

    # for letter in string.ascii_letters:
    #     list.append(letter)
    #
    #     shuffle(list)
    #
    #     new_list = (list[0:5])


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    success_url = "/"
    fields = ('title', 'description', 'url', 'newrl', 'private')

    def get_object(self):
        return Bookmark.objects.get(pk=self.kwargs.get('pk'), user=self.request.user)


class ProfileDetailView(DetailView):
    model = Profile


class ProfileListView(ListView):
    model = Profile
