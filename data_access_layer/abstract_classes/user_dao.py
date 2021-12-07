from abc import ABC, abstractmethod


class UserDAO(ABC):

    # create player method
    @abstractmethod
    def create_user_entry(self, account: User) -> User:
        pass

    # get player information
    @abstractmethod
    def get_user_information(self, user_id: int) -> User:
        pass

    # get all player information
    @abstractmethod
    def get_all_user_information(self) -> list[User]:
        pass

    # update player information
    @abstractmethod
    def update_user_information(self, user: User) -> User:
        pass

    # delete player information
    @abstractmethod
    def delete_user_information(self, user_id: int) -> bool:
        pass
