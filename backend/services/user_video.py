from repositories.repo import AbstractRepository
from shema.user_video import UserVideoIn
from shema.user import UserDB

def neuro(d):
    return [i.video_id for i in d] 
    
    



class UserVideoService:
    def __init__(self, user_video_repository: AbstractRepository, user_repository: AbstractRepository, video_repository: AbstractRepository):
        self.user_repository: AbstractRepository = user_repository
        self.user_video_repository: AbstractRepository = user_video_repository 
        self.video_repository: AbstractRepository =  video_repository

    def create(self, user_video_info: UserVideoIn):
        return self.user_video_repository.create(user_video_info)


    def get_videos(self, user_video_info: list[UserVideoIn]) -> list[UserVideoIn]:
        res = []  
        print(";asldkfj;laskdjf;lkasdjrfa;lkjslk;j")
        if not self.user_repository.read_by_options({"cookies": user_video_info[0].cookies}):
            self.user_repository.create(UserDB(cookies =user_video_info[0].cookies))

        for one in user_video_info:
            self.create(one)
        new_videos = neuro(self.read_by_options({"cookies": user_video_info[0].cookies}))
        new_videos_finded = [self.video_repository.read_by_options({"id_hash": video_with_out_inf})[0] for video_with_out_inf in new_videos] 
        for i in new_videos_finded:
            print(i.title)

        return new_videos_finded 


    
    def read_by_options(self, options: dict):
        return self.user_video_repository.read_by_options(options)
    

