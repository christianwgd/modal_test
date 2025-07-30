from django.shortcuts import redirect
from django.urls import reverse


def index(request):  # pylint: disable=unused-argument
    return redirect(reverse('blog:index'))
