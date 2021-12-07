from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def __init__(self, user_name: str, user_password: str):
        pass

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def get_user(self):
        pass

    @abstractmethod
    def update_user(self):
        pass

    @abstractmethod
    def update_user(self):
        pass

    @abstractmethod
    def get_all_user(self):
