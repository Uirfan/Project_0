from abc import ABC, abstractmethod

from entities.accounts import Account


class AccountDAO(ABC):

    @abstractmethod
    def create_account_entry(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_account_information(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def get_all_account_information(self) -> list[Account]:
        pass

    @abstractmethod
    def update_account_information(self, account: Account) -> Account:
        pass

    @abstractmethod
    def delete_account_information(self, account_id: int) -> bool:
        pass
