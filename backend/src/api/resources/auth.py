from ..middleware.auth import auth_required
from sanic_restplus import Resource
from sanic.request import Request
from sanic import response as res
import bcrypt

from ..models import user, UserDAO, User
from .. import auth_ns as ns

DAO = UserDAO()


@ns.route("/")
class Auth(Resource):
    """
    Authentication routes
    """

    @ns.doc("get current user")
    @ns.marshal_list_with(user)
    @auth_required
    async def get(self, request: Request):
        """
        Get the current user from the request session.
        If the user is not authenticated it will send an error.
        (see @auth_required in middleware/)
        """
        return request.ctx.session.get("user")

    @ns.doc("login")
    @ns.expect(user)
    @ns.marshal_with(user, code=200)
    async def post(self, request: Request):
        """Create a new user"""
        raw_user: User = request.json
        try:
            user = DAO.findByUsername(raw_user.username)
            if not bcrypt.checkpw(raw_user, user.password):
                return {"error": "Invalid credentials"}, 401
            return user
        except:
            return {"error": f"User {raw_user.username} not found"}, 404
