from django.contrib import admin

from shopify_install.models import Token

class TokenAdmin(admin.ModelAdmin):
    list_display = ['token', 'shop']
    list_filter = ['shop']
    search_fields = ['token', 'shop']

admin.site.register(Token, TokenAdmin)
