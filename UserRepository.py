import uuid

class UserRepository:
    def __init__(self, mongo):
        self.mongo = mongo

    def create_user(self, user: dict):
        user['_id'] = str(uuid.uuid4())
        try:
            self.mongo.insert_one(user)
        except Exception as e:
            raise e

    def find_user(self, user):
        try:
            self.mongo.find({ 'email': user['email']})
        except Exception as e:
            raise e