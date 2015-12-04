from django.contrib import admin
from pools.models import Pools

admin.site.register(Pools)


class AuthorAdmin(admin.ModelAdmin):
    pass
#admin.site.register(Author, AuthorAdmin)
# Register your models here.
