from django.contrib import admin
from .models import Page  # import the Page model
# create the PageAdmin class, which inherits from the ModelAdmin class
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Page, PageAdmin)  # register the Page & PageAdmin models with the admin
