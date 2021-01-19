from inspect import isawaitable
from sanic.request import Request
from sanic import response as res
from .. import api
from ..models import UserDAO

DAO = UserDAO()

# TODO: permissions


def auth_required(func):
    """ adds auth user to request session """

    async def wrapper(_, request: Request, *args):
        if (
            request.ctx.session
            and request.ctx.session.get("user_id")
            and request.ctx.session.get("user_id") != ""
        ):
            user = DAO.get(request.ctx.session.get("user_id"))
            if user:
                request.ctx.session.user = user
                response = func(request, *args)
                if isawaitable(response):
                    response = await response
                return response
            else:
                return api.abort(403, "Not authenticated")

        else:
            return api.abort(403, "Not authenticated")

    return wrapper