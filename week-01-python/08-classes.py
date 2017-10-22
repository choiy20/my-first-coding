# 클래스 class

##### Articls variables
title1 = "programming"
author1 = "marco"
content1 = "programming is easy"
view_count1 = 0

title2 = "coaching"
author2 = "marco"
content2 = "coaching is easy"
view_content2 = 0

title3 = "startup"
author3 = "marco"
content3 = "startup is easy"
view_content3 = 0

##### Article class
# class Article:
#     title = "programming"
#     author = "marco"
#     content = "programming is easy"
#     view_count = 0
#
# article1 = Article()
# print(article1.title)
# article2 = Article()
# article2.title = "coaching"
# print(article1.title)
# print(article2.title)

##### Article class with __init__
# class Article:
#         author = "marco"
#         view_count = 0
#
#         def __init__(self, title, content):
#             self.title = title
#             self.content = content
#
#         def read(self): #나만의 read라는 함수지정
#             self.view_count = self.view_count + 1
#
#
# article1 = Article("programming", "developing is easy")
# article2 = Article("coaching", "coaching is easy")
# article3 = Article("startup", "startup is easy")
#
# # print(article1.view_count)
# # article1.read()
# print(article1.title)


##### Article class inheritance 상속
# class BrunchArticle(Article): #복사 붙여넣기 할 필요없이 article을 괄호안에 넣어주면 됨
#
#     source = "Brunch"
#
# brunch_article = BrunchArticle ("programming", "programming is easy") #instance 만들어 주기
# print(brunch_article.title)
# print (brunch_article.source) # 새로 추가한 변수 확인
# print (brunch_article.view_count)
# brunch_article.read()
# print(brunch_article.view_count)

# class Article:
#         author = "marco"
#         view_count = 0
#
#         def __init__(self, title, content):
#             self.title = title
#             self.content = content
#
#         def read(self): #나만의 read라는 함수지정
#             self.view_count = self.view_count + 1
#
#
# article1 = Article("programming", "developing is easy")
# article1 = Article("coaching", "coaching is easy")
# article1 = Article("startup", "startup is easy")
class School:
    def __init__(self, name, date, address):
        self.name = name
        self.date = date
        self.address = address

school1 = School("nanyang", "21-Oct-2017", "Yio Chu Kang")

print(school1.name)
