from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from main import models
from main.forms import CustomUserChangeForm

# Admin Custom Page
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm

    list_display    = ("email", "is_staff", "is_active", 'is_superuser',)
    list_filter     = ("email", "is_staff", "is_active", 'is_superuser',)
    fieldsets = (
        ("User Info", {'fields': (('email', 'email_confirmed'), 'password', ('phone', 'phone_confirmed',),)}),
        ('Personal Info', {'fields': ('first_name', 'last_name','country', 'city',
                                      'profile_picture', 'bio')}),
        ("Permission", {"fields": ("is_staff", "is_active",'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields   = ("email",)
    ordering        = ("email",)


# Properties Models
admin.site.register(models.Property)
admin.site.register(models.PropertyImagesVideos)

# Users Models
admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.AuthTokens)
admin.site.register(models.EmailPhoneConfirmation)
admin.site.register(models.UserNotification)
admin.site.register(models.Wishlist)
admin.site.register(models.WistlistItem)
