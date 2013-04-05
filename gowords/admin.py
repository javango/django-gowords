from django.contrib import admin

from gowords.models import Goword

class GowordAdmin(admin.ModelAdmin):
    list_display = ('slug','url',)
    
admin.site.register(Goword, GowordAdmin)