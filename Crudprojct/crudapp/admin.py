from django.contrib import admin
from crudapp.models import StudentModel

# Register your models here.
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','phone','email','address']