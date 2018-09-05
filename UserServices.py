from repositories.UserRepository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: dict):
        user['nome'] = str(user['nome'])
        user['senha'] = str(user['senha'])
        user['email'] = str(user['email'])
        user = self.user_repository.create_user(user)
        return user

    def find_user(self, user):
        user = self.user_repository.find_user(user)
        return user