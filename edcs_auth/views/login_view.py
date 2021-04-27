from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LoginView as BaseLoginView


class LoginView(BaseLoginView):
    template_name = f"edcs_auth/bootstrap{settings.EDCS_BOOTSTRAP}/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session.set_test_cookie()
        if not self.request.session.test_cookie_worked():
            messages.add_message(self.request, messages.ERROR, "Please enable cookies.")
        self.request.session.delete_test_cookie()
        return context
