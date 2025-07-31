from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

from blog.models import BlogPost


class BlogPostForm(BSModalModelForm):

    class Meta:
        model = BlogPost
        fields = [
            'title', 'content'
        ]

    def clean_title(self):
        print("I'm cleaning title")
        print(self.cleaned_data)
        title = self.cleaned_data.get('title')
        if "a" not in title:
            print('no letter "a" found in title')
            raise forms.ValidationError("Must have the letter 'a' in the title")
        print('letter "a" found in title')
        return title