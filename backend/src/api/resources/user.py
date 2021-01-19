from ..middleware.auth import auth_required
from sanic_restplus import Resource
from sanic.request import Request

from ..models import user, UserDAO
from .. import users_ns as ns

DAO = UserDAO()


@ns.route("/")
class UseList(Resource):
    """Shows a list of all userss, and lets you POST to add new users"""

    @ns.doc("list")
    @ns.marshal_list_with(user)
    async def get(self, request: Request):
        """List all users"""
        return DAO.get_all()

    @ns.doc("create")
    @ns.expect(user)
    @ns.marshal_with(user, code=201)
    async def post(self, request: Request):
        """Create a new user"""
        return DAO.create(request.json), 201


@ns.route("/<id:int>")
@ns.response(404, "User not found")
@ns.param("id", "The user identifier")
class User(Resource):
    """Show a single user and lets you delete them"""

    @ns.doc("get")
    @ns.marshal_with(user)
    @auth_required
    async def get(self, request, id):
        """Fetch a given resource"""
        return DAO.get(id)

    @ns.doc("delete_todo")
    @ns.response(204, "User deleted")
    @auth_required
    async def delete(self, request, id):
        """Delete a user given its identifier"""
        DAO.delete(id)
        return "", 204

    @ns.expect(user)
    @ns.marshal_with(user)
    @auth_required
    async def put(self, request, id):
        """Update a user given its identifier"""
        return DAO.update(id, request.json)
