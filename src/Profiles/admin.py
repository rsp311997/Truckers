from csv import list_dialects
from django.contrib import admin
from Profiles.models import Profile,LicenseImage

# Register your models here.


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ['mobile','profileImg','role','userID']

class LicenseImagesAdmin(admin.ModelAdmin):
    list_display= ('licenseImg','profileID')

admin.site.register(Profile,ProfilesAdmin)
admin.site.register(LicenseImage,LicenseImagesAdmin)