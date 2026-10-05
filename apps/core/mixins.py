from typing import Any, cast

from django.contrib import messages
from django.forms import BaseModelForm
from django.http import HttpResponse


class SuccessMessageMixin:
    success_message: str = ""
    request: Any  # Fourni par la vue Django qui utilise ce mixin

    def form_valid(self, form: BaseModelForm[Any]) -> HttpResponse:
        response = cast(HttpResponse, super().form_valid(form))  # type: ignore[misc]
        if self.success_message:
            messages.success(self.request, self.success_message)
        return response
