from abc import ABC, abstractmethod
from typing import List
from features.blacklist.domain.models import BlacklistUser


class BlacklistRepository(ABC):
    @abstractmethod
    def add_user(self, user: BlacklistUser) -> None:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> BlacklistUser:
        pass

    @abstractmethod
    def get_all_users(self) -> List[BlacklistUser]:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass
