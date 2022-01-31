from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect


class SubjectAdminMethodsMixin:
    def post_url_on_delete_kwargs(self, request, obj):
        return {}

    def response_post_save_add(self, request, obj):
        self.clear_message(request)
        return redirect(self.next(request))

    def response_post_save_change(self, request, obj):
        self.clear_message(request)
        return redirect(self.next(request))

    def clear_message(self, request):
        storage = messages.get_messages(request)
        for msg in storage:
            pass
        storage.used = True

    def next(self, request):
        return reverse(request.GET.get('next', None), args=[request.GET.get('subject'), request.GET.get('appointment')])
