from repositories.repo import AbstractRepository
from shema.user_video import UserVideoIn


def neuro(d):
    return d
    
    



class UserVideoService:
    def __init__(self, user_video_repository: AbstractRepository, user_repository: AbstractRepository, video_repository: AbstractRepository):
        self.user_repository: AbstractRepository = user_repository
        self.user_video_repository: AbstractRepository = user_video_repository 
        self.video_repository: AbstractRepository =  video_repository

    def create(self, user_video_info: UserVideoIn):
        return self.user_video_repository.create(user_video_info)


    def get_videos(self, user_video_info: list[UserVideoIn]) -> list[UserVideoIn]:
        res = []  
        for one in user_video_info:
            self.create(one)
        new_videos = neuro(self.read_by_options({"cookies": user_video_info[0].cookies}))
        return new_videos


    
    def read_by_options(self, options: dict):
        return self.user_video_repository.read_by_options(options)
    

