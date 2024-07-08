from django.contrib import admin
from .models import  *
# Register your models here.


class ShowUserdata(admin.ModelAdmin):
    list_display = ['First_name','Last_name','Email','Password','Phone','Data_submitted_at']
admin.site.register(User_table,ShowUserdata)
