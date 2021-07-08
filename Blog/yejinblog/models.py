from django.db import models

class Project(models.Model):
     # 필요한 필드와 필드 옵션은 그때그때 검색해서 찾는게 더 낫당 
    title = models.CharField(max_length=200)
    project_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField()    # 날짜와 시간을 정해주는 필드
    body = models.TextField()     # 본문 (제한없는 text 필드)

    # 어디선가 객체가 호출이 되었을 때, 나오는 이름 설정
    def __str__(self):
        return self.title #글의 제목으로 설정

class Project_ing(models.Model):
     # 필요한 필드와 필드 옵션은 그때그때 검색해서 찾는게 더 낫당 
    title_ing = models.CharField(max_length=200)
    project_name_ing = models.CharField(max_length=100)
    pub_date_ing = models.DateTimeField()    # 날짜와 시간을 정해주는 필드
    body_ing = models.TextField()     # 본문 (제한없는 text 필드)

    # 어디선가 객체가 호출이 되었을 때, 나오는 이름 설정
    def __str__(self):
        return self.title_ing #글의 제목으로 설정
