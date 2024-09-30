from repositories.repo import AbstractRepository
from shema.user import UserIn



class UserService:
    def __init__(self, user_repository: AbstractRepository):
        self.user_repository: AbstractRepository = user_repository 

    def create(self, user_info: UserIn):
        return self.user_repository.create(user_info)

