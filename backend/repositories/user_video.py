from repositories.repo import SqlAlchemyRepository
from models.user_video import UserVideo 

class UserVideoRepository(SqlAlchemyRepository):

    def __init__(self, session):
        self.session = session
        super().__init__(session, UserVideo) 
