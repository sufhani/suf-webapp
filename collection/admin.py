from django.contrib import admin

# Register your models here.
from collection.models import Thing

#set up automated
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description',)
    prepoluted_fields = {'slug': ('name',)}


admin.site.register(Thing, ThingAdmin)