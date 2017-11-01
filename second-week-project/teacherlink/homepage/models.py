from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    like_count = models.IntegerField()

    def __str__(self): #두개의 언더바는 내부에서 쓰기위함이다.
        return "{} ({})".format(self.name, self.like_count) #Article제목이 그대로 나오게 해줌

class Comment(models.Model):
    course = models.ForeignKey(Course)
    comment = models.CharField(max_length=100)
