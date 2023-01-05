from django.db import models
from django.forms import CharField


# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.CharField(max_length = 50)
    snsimage = models.ImageField(upload_to = '')
    # null model中にnullが入っても大丈夫　black formが空でも問題ない
    good = models.IntegerField(null=True, blank=True, default=1)
    read = models.IntegerField(null=True, blank=True, default=1)
    readtext = models.TextField(null=True, blank=True, default='a')
