from django.contrib import admin
from v1.models import Number, Colab

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Colab, AuthorAdmin)
admin.site.register(Number, AuthorAdmin)