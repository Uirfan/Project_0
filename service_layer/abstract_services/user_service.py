from abc import ABC, abstractmethod

from entities.users import User


class UserService(ABC):

    # create user method
    @abstractmethod
    def service_create_user_entry(self, user: User) -> User:
        pass

    # get user information
    @abstractmethod
    def service_get_user_information(self, user_id: int) -> User:
        pass

    # get all user information
    @abstractmethod
    def service_get_all_users_information(self) -> list[User]:
        pass

    # update user information
    @abstractmethod
    def service_update_user_information(self, user: User) -> User:
        pass

    # delete user information
    @abstractmethod
    def service_delete_user_information(self, user_id: int) -> bool:
        pass
