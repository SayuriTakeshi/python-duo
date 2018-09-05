from tinymongo import TinyMongoClient as TMC
from services.UserServices import UserService
from repositories.UserRepository import UserRepository


con = TMC()
db = con.db_duo
collection_users = db.users

user_service = UserService(UserRepository(collection_users))
user_find = UserService(UserRepository(collection_users))