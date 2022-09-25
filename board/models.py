from django.db import models

# Create your models here.
class Notice(models.Model):

    title       = models.CharField(max_length=200, verbose_name="제목")
    contents    = models.TextField(verbose_name="내용")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at  = models.DateTimeField(auto_now=True, verbose_name="최종수정일")
    hit = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.title
