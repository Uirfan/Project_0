from abc import ABC, abstractmethod

class AccountDAO(ABC):

    # create player method
    @abstractmethod
    def create_account_entry(self, account: Account) -> Account:
        pass

    # get player information
    @abstractmethod
    def get_account_information(self, account_id: int) -> Account:
        pass

    # get all player information
    @abstractmethod
    def get_all_accounts_information(self) -> list[Account]:
        pass

    # update player information
    @abstractmethod
    def update_account_information(self, account: Account) -> Account:
        pass

    # delete player information
    @abstractmethod
    def delete_player_information(self, account_id: int) -> bool:
        pass
