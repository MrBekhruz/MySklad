from django.contrib import admin
from .models import *


class PostUser(admin.ModelAdmin):
    list_display = ('user_full_name','about','user_age','position_name',)
admin.site.register(User,PostUser)

class Baza(admin.ModelAdmin):
    list_display = ('products','brend','color',)
admin.site.register(BazaItems,Baza)
class NameClient(admin.ModelAdmin):
    list_display=('name','phone_number','register_time','receptionist',)
admin.site.register(Client,NameClient)
admin.site.register(ServiceName)
admin.site.register(ServiceXizmati)
admin.site.register(EndService)
admin.site.register(ReturnService)
