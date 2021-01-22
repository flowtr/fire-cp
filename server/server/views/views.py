import json
from typing import Union
from django.http import JsonResponse, HttpRequest
from django.views import View
from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.forms.models import model_to_dict


def build_response(code: int, data="", error: Union[str, Exception] = None):
    return JsonResponse(
        {"ok": True if code == 200 else False, "data": data, "error": error},
        safe=False,
        status=code,
    )


def home_view():
    return build_response(
        200, data="Hello World! Welcome to your Flowtr Panel instance."
    )


class AuthView(View):
    def post(_, request: HttpRequest):
        json_data = json.loads(request.body)
        user = authenticate(
            request,
            username=json_data["username"],
            password=json_data["password"],
        )
        if user is not None:
            login(request, user)
            return build_response(200, data=model_to_dict(user))
        else:
            return build_response(401, error="Invalid Credentials")

    def get(_, request: HttpRequest):
        user = request.user
        if request.user.is_authenticated:
            return build_response(200, data=model_to_dict(user))
        else:
            return build_response(403, error="Not Authenticated")
