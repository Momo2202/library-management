from django.contrib import messages

class SuccessMessageMixin:
    success_message = ""
    def form_valid(self, form):
        response=super().form_valid(form)
        if self.success_message:
            messages.success(self.request, self.success_message)
        return response