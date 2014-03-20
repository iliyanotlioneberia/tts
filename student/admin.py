from django.contrib import admin
from student.models import Student, Module

class StudentAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}
        list_display = ('name', 'module', 'stnumber')
        search_fields = ['name']

class ModuleAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}

admin.site.register(Student, StudentAdmin)
admin.site.register(Module, ModuleAdmin)
