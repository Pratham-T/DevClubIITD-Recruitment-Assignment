from django.contrib import admin
from django.contrib.admin.forms import AdminAuthenticationForm
import types

# Restricted admin site access to Librarians
def has_permission(self, request):
    return request.user.is_active and (
        request.user.is_staff
        or request.user.groups.filter(name='Librarian').exists()
    )


class GrpAdminAuthenticationForm(AdminAuthenticationForm):
    def confirm_login_allowed(self, user):
        if user.groups.filter(name='Librarian').exists():
            user.is_staff = True
        super().confirm_login_allowed(user)


admin.site.login_form = GrpAdminAuthenticationForm
admin.site.has_permission = types.MethodType(has_permission, admin.site)


# Register your models here.
