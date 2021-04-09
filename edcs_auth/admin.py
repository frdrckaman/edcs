from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import UserProfile

admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "User profile"
    filter_horizontal = ("sites",)


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
    )


class UserProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ("sites",)
    list_display = (
        "user",
        "mobile",
        "user_sites",
    )

    # if you want to include foreignKey value on list_display
    def user_sites(self, obj=None):
        return mark_safe(
            "<BR>".join([o.name for o in obj.sites.all().order_by("name")])
        )


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
