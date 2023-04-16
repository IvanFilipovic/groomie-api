from django.contrib import admin
from .models import Guest, UniqueWedding, BasicGuest, BasicWedding
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field


class WeddingInline(admin.StackedInline):
    model = Guest
    fields = (('wedding_owner', 'guest_fname', 'guest_lname', 'plusone_fname', 'plusone_lname'), 'guest_type',('couple', 'plusone', 'coming', 'kids'), 'message')
    extra = 0

@admin.register(UniqueWedding)
class WeddingAdmin(admin.ModelAdmin):
    inlines = [
        WeddingInline,
    ]

class GuestResource(resources.ModelResource):
    class Meta:
        model = Guest
        guest_slug = Field(attribute='guest_slug', column_name='guest_slug')
        wedding_owner = Field(attribute='wedding_owner', column_name='wedding_owner')
        guest_fname = Field(attribute='guest_fname', column_name='guest_fname')
        guest_lname = Field(attribute='guest_lname', column_name='guest_lname')
        plusone_fname = Field(attribute='plusone_fname', column_name='plusone_fname')
        plusone_lname = Field(attribute='plusone_lname', column_name='plusone_lname')
        guest_type = Field(attribute='guest_type', column_name='guest_type')
        import_id_fields = ('guest_slug',)        
        fields = ('guest_slug', 'wedding_owner', 'guest_fname', 'guest_lname', 'plusone_fname', 'plusone_lname', 'guest_type',)
        exclude = ('id', 'couple', 'plusone', 'coming', 'kids', 'message',)

class GuestAdmin(ImportExportModelAdmin):
    resource_classes = [GuestResource]

admin.site.register(Guest, GuestAdmin)
admin.site.register(BasicGuest)
admin.site.register(BasicWedding)
