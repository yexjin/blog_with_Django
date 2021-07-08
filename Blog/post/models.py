from django.db import models

class Post(models.Model): # post 테이블 만들기
    title = models.CharField(max_length=100) # 텍스트가 100이하로 제한!
    content = models.TextField(max_length=1000) #천자이상 쓰면안된다.

