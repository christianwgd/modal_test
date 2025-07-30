from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

from blog.models import BlogPost


class BlogPostForm(BSModalModelForm):

    class Meta:
        model = BlogPost
        fields = [
            'title', 'content'
        ]

