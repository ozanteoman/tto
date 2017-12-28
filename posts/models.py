from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    user = models.ForeignKey(User,default=1)#iliskilendirme one-to-many
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = models.TextField(max_length=1000,verbose_name="İçerik")
    image = models.ImageField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ="Gönderiler"
        ordering=["-id"]

    def __str__(self):
        return "%s %s"%(self.title,self.created_date)

class Comments(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Posts)
    content = models.TextField(verbose_name='Icerik.')

    def __str__(self):
        return '%s-%s'%(self.user,self.post)
    class Meta:
        verbose_name_plural='Yorumlar'



