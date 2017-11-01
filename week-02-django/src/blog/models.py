from django.db import models

# Create your models here.
class Article(models.Model): #Model 이라는 클래스를 상속받음.
    title = models.CharField(max_length=30) #Title의 성격은 문자다라고 표현해줌.
    contents = models.TextField()
    view_count = models.IntegerField()

    def __str__(self): #두개의 언더바는 내부에서 쓰기위함이다.
        return "{} ({})".format(self.title, self.view_count) #Article제목이 그대로 나오게 해줌

class Comment(models.Model):
    article = models.ForeignKey(Article) #위에 Article을 가져와줌
    comment = models.CharField(max_length=100)
