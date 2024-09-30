from repositories.repo import SqlAlchemyRepository
from models.video import Video

class VideoRepository(SqlAlchemyRepository):

    def __init__(self, session):
        self.session = session
        super().__init__(session, Video)

