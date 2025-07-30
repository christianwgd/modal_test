from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _

from blog.forms import BlogPostForm
from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost


class BlogPostCreateView(BSModalCreateView):
    model = BlogPost
    form_class = BlogPostForm
    success_message = _('blog post saved')
    success_url = reverse_lazy('home')


class BlogPostUpdateView(BSModalUpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_message = _('blog post saved')
    success_url = reverse_lazy('home')
