from django.contrib import admin
from myapp import models
from myapp.models import Client, Immobile, ImmobileImage, RegisterLocation

# admin.site.register(Immobile)
# admin.site.register(ImmobileImage)

admin.site.register(Client)
admin.site.register(RegisterLocation)

class ImmobileImageInlineAdmin(admin.TabularInline):
    model = models.ImmobileImage
    extra = 0
    
class ImmobileAdmin(admin.ModelAdmin):
    inlines = [ImmobileImageInlineAdmin]
    
admin.site.register(models.Immobile, ImmobileAdmin)