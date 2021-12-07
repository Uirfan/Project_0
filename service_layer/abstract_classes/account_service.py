from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def __init__(self, user_name: str, user_password: str):
        pass

    @abstractmethod
    def create_account(self):
        pass

    @abstractmethod
    def get_account(self):
        pass

    @abstractmethod
    def update_account(self):
        pass

    @abstractmethod
    def update_account(self):
        pass

    @abstractmethod
    def get_all_accounts(self):
        pass

