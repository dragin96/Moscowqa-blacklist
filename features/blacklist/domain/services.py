from features.blacklist.domain.ports import BlacklistRepository
from features.blacklist.domain.models import BlacklistUser

class BlacklistService:
    def __init__(self, repository: BlacklistRepository):
        self.repository = repository

    def add_user_to_blacklist(self, user: BlacklistUser):
        self.repository.add_user(user)

    def get_user(self, user_id: int):
        return self.repository.get_user(user_id)

    def get_all_users(self):
        return self.repository.get_all_users()

    def remove_user(self, user_id: int):
        self.repository.delete_user(user_id)