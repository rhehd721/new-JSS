from django.db import models
from django.contrib.auth.models import User


# 자소설 작성 모댈 
class Jasoseol(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# 댓글 모델 작성
class Comment(models.Model):
    content = models.CharField( max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Jasoseol = models.ForeignKey(Jasoseol,on_delete=models.CASCADE)