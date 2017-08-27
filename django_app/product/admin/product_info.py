from django.contrib import admin


class VinylInfoAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'thickness',
        'material',
    )
    list_editable = (
        'thickness',
        'material',
    )
