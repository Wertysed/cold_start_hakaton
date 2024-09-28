from repositories.repo import SqlAlchemyRepository
from models.user import User 

class UserRepository(SqlAlchemyRepository):

    def __init__(self, session):
        self.session = session
        super().__init__(session, User) 
