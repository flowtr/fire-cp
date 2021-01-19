from sanic_restplus import fields
from sanic_restplus.errors import abort
from .. import api
from ...config import mongo
from dataclasses import dataclass
import bcrypt

user = api.model(
    "User",
    {
        "_id": fields.String(readOnly=True, description="Unique id from mongodb"),
        "username": fields.String(required=True, description="Username"),
        "salt": fields.String(required=True, description="password salt"),
        "password": fields.String(required=True, description="hashed password"),
    },
)


@dataclass()
class User:
    _id: str
    username: str
    salt: str
    password: str


class UserDAO(object):
    def __init__(self) -> None:
        self.db = mongo["users"]

    def get_all(self) -> User:
        try:
            return self.db.find()
        except:
            return api.abort(404, f"User {id} doesn't exist")

    def get(self, id: str) -> User:
        user = self.db.find_one({"_id": {"$in": [id]}})
        if user is None:
            api.abort(404, f"User {id} doesn't exist")
        return user

    def findByUsername(self, username: str) -> User:
        user = self.db.find_one({"username": {"$in": [username], "$nin": [None, ""]}})
        if user is None:
            api.abort(404, f"User {id} doesn't exist")
        return user

    def create(self, data: User) -> User:
        username = data["username"]
        if self.findByUsername(username=username):
            return abort(400, f"User {username} already exists")
        data["salt"] = bcrypt.gensalt()
        data["password"] = bcrypt.hashpw(data["password"], data["salt"])

        user = self.db.insert_one(data)

        return self.get(user.inserted_id)

    def change_password(self, id: str, data: User) -> User:
        existing_user = self.db.find_one({"_id": id})
        if existing_user and bcrypt.checkpw(data["password"], existing_user["salt"]):
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(data["password"], salt)
            data["password"] = hashed

        return data

    def update(self, id: str, data: User) -> User:
        if data.password and data.password != "":
            data = self.change_password(id, data)

        self.db.update_one({"_id": id}, data)
        return self.get(id)

    def delete(self, id: str):
        self.db.delete_one({"_id": id})
        return {"success": f"Deleted user {id}"}