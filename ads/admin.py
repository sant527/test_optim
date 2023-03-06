from django.contrib import admin

# Register your models here.
from .models import Ads

from django.db.models import ManyToOneRel, ForeignKey, OneToOneField


MySpecialAdmin = lambda model: type('SubClass'+model.__name__, (admin.ModelAdmin,), {
    'list_display': [x.name for x in model._meta.fields],
    'list_select_related': [x.name for x in model._meta.fields if isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField,))]
})

#admin.site.unregister(Ads)
admin.site.register(Ads, MySpecialAdmin(Ads))

# class AdsAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Ads._meta.get_fields()]


# admin.site.register(AdsAdmin)