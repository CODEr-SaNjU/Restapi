from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserProfileCreationForm, UserProfileChangeForm
from .models import UserProfile, LeadGenerator


class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    list_display = ['email', 'first_name','last_name','user_type', 'mob_number', 'admin', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email',  'password')}),
        ('Personal Info', {
            'fields': ('first_name','last_name', 'mob_number','user_type')}),
        ('Permissions', {'fields': ('date_joined', 'is_staff',
                                    'is_active', 'admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',  'password1', 'password2', 'is_staff', 'is_active', 'admin')}
         ),
    )
    search_fields = ['email', 'mob_number', 'first_name']
    ordering = ['email', 'mob_number']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(LeadGenerator)