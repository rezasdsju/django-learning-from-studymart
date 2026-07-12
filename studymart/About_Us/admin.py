from django.contrib import admin
from About_Us.models import Teachers
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'tid', 'tname', 'temail')
admin.site.register(Teachers, TeacherAdmin)