from django.db import models
from django.utils.translation import gettext_lazy as _


class BlogPost(models.Model):

    class Meta:
        verbose_name = _("Blog post")
        verbose_name_plural = _("Blog posts")
        ordering = ("title",)

    def __str__(self):
        return self.title

    title = models.CharField(
        verbose_name=_('Title'), max_length=20
    )
    content = models.TextField(verbose_name=_('Content'))