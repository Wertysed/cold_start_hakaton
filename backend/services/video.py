from repositories.repo import AbstractRepository
from shema.video import Video 



class VideoService:
    def __init__(self, video_repository: AbstractRepository):
        self.video_repository: AbstractRepository = video_repository 

    def create(self, video_info: Video):
        return self.video_repository.create(video_info)

    def read_by_options(self, options: dict):
        return self.video_repository.read_by_options(options)
    
