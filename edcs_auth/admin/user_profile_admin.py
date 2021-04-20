from django.contrib import admin
from django.utils.safestring import mark_safe

from ..forms import UserProfileForm
from ..models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "User profile"

    filter_horizontal = ("sites", "roles")

    form = UserProfileForm


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    filter_horizontal = ("sites",)

    list_display = (
        "user",
        "user_sites",
        "mobile",
    )

    @staticmethod
    def user_sites(obj=None):

        return mark_safe(
            "<BR>".join([o.name for o in obj.sites.all().order_by("name")])
        )

