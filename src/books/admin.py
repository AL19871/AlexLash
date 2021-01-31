from django.contrib import admin

from .models import Autors, Addresses, Cities, Genres, Publishers

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'address')
    search_fields = ['last_name', 'first_name', 'address__city__name']

class AddressesAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'block', 'house')
    search_fields = ['city', 'street']

class CitiesAdmin(admin.ModelAdmin):
    pass

class GenresAdmin(admin.ModelAdmin):
    pass

class PublishersAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

admin.site.register(Autors, AuthorsAdmin)
admin.site.register(Addresses, AddressesAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Publishers, PublishersAdmin)
