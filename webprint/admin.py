from django.contrib import admin

from .models import Print, PrintImg


class PrintImgInline(admin.TabularInline):
    model = PrintImg


@admin.register(Print)
class PrintAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_date', 'expires_in', 'ip']
    date_hierarchy = 'pub_date'
    search_fields = ['name', 'ip']
    ordering = ['-pub_date']
    inlines = [PrintImgInline]
