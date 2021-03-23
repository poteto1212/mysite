from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    
    #publish(self)メソッド→ブログ公開に必要となる
    #公開日時(published_dateカラムのデフォルト値を決める為に必要なメソッド)
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    
    #大分類名をtitleに指定する       
    def __str__(self):
        return self.title