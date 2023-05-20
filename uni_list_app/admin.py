from django.contrib import admin

# Register your models here.
from django.contrib import admin
from uni_list_app.models import UniList, UniItem

admin.site.register(UniItem)
admin.site.register(UniList)
