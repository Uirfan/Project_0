from abc import ABC, abstractmethod

from entities.accounts import Account


class AccountService(ABC):

    # create account method
    @abstractmethod
    def service_create_account_entry(self, account: Account) -> Account:
        pass

    # get account information
    @abstractmethod
    def service_get_account_information(self, account_id: int) -> Account:
        pass

    # get all account information
    @abstractmethod
    def service_get_all_accounts_information(self) -> list[Account]:
        pass

    # update account information
    @abstractmethod
    def service_update_account_information(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_transfer_fund_account(self, accountId, account_to_transferId, amount) -> Account:
        pass

    # delete account information
    @abstractmethod
    def service_delete_account_information(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def service_withdraw_funds(self, account_id, amount: float):
        pass

    @abstractmethod
    def service_deposit_funds(self, account_id, amount: float):
        pass

