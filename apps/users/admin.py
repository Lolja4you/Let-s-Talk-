from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUsers
from users.forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUsersAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUsers
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active', 'date_joined',)
    list_display_links = ('username', 'email', 'is_staff', 'is_superuser', 'is_active', 'date_joined',)
    list_filter = ('date_joined', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {
            'fields' : ('email', 'username', 'password', 'aboutUser',)
        }),
        ('Permissions', {
            'fields': ('photoUser', 'is_staff', 'is_superuser', 'is_active', 'groups',)
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_superuser', 'groups',)
        }),
    )

    search_fields = ('email', 'username',)
    ordering = ('email', 'username',)

'''class CustomGroupAdmin(admin.ModelAdmin):
    #search_fields = ('name',)
    #ordering = ('name',)
    #filter_horizontal = ('permissions',)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'permissions':
            qs = kwargs.get('queryset', db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs['queryset'] = qs.select_related('content_type')
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)'''



admin.site.register(CustomUsers, CustomUsersAdmin)
#admin.site.register(CustomGroupModel, CustomGroupAdmin)
