'''
Created on 11 Jan 2024

@author: mpayen
'''

from django.contrib import admin
from website.models import Foodtruck, Message, Menu, MenuItem

class FoodtruckAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'email', 'numero_de_telephone')
    
    # This will help you to disable add functionality
    def has_add_permission(self, request):
        if Foodtruck.objects.exists():
            return False
        
        return True

admin.site.register(Foodtruck, FoodtruckAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('date_de_publication', 'nom', 'email', 'contenu')

admin.site.register(Message, MessageAdmin) 


class MenuItemAdmin(admin.TabularInline):
    list_display = ('nom', 'description', 'prix')
    
    model = MenuItem
    extra = 1
    

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemAdmin]
    list_display = ('nom',)

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem) 