from sanic_restplus import Api

api = Api(version="1.0", title="Flowtr Panel", description="Flowtr panel backend")
users_ns = api.namespace("v1/users", description="")
auth_ns = api.namespace("v1/auth", description="Authentication routes")

api.add_namespace(users_ns)
api.add_namespace(auth_ns)
