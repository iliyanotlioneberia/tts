from django.contrib import admin
from pages.models import HomePage

class TinyAdmin(admin.ModelAdmin):
        class Media:
                js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas.js',)

admin.site.register(HomePage, TinyAdmin)
