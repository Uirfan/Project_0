from abc import ABC, abstractmethod

from entities.users import User


class UserDAO(ABC):

    @abstractmethod
    def create_user_entry(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_information(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_all_user_information(self) -> list[User]:
        pass

    @abstractmethod
    def update_user_information(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user_information(self, user_id: int) -> bool:
        pass
