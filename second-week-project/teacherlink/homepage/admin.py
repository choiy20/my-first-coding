from django.contrib import admin
from .models import Course, Comment
# Register your models here.
@admin.register(Course, Comment)
class HomepageAdmin(admin.ModelAdmin):
    pass
# Register your models here.
