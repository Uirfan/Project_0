from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDao
from data_access_layer.implementation_classes.user_postgres_dao import UserPostgresDao
from entities.accounts import Account
from service_layer.abstract_services.account_service import AccountService
from custom_exceptions.custom_exception_message import CustomExceptionMessage


class AccountServiceImp(AccountService):
    def __init__(self, account_dao, user_dao):
        self.account_dao: AccountPostgresDao = account_dao
        self.user_dao: UserPostgresDao = user_dao

    def service_create_account_entry(self, account: Account) -> Account:
        existing_users = self.user_dao.get_all_user_information()
        for a in existing_users:
            if a.user_id == account.user_id:
                return self.account_dao.create_account_entry(account)
        raise CustomExceptionMessage("User ID not found")

    def service_get_account_information(self, account_id: int) -> Account:
        existing_account = self.service_get_all_accounts_information()
        for a in existing_account:
            if a.account_id == account_id:
                return self.account_dao.get_account_information(account_id)
        raise CustomExceptionMessage("Account not found")

    def service_get_all_accounts_information(self) -> list[Account]:
        return self.account_dao.get_all_account_information()

    def service_update_account_information(self, account: Account) -> Account:
        existing_account = self.service_get_all_accounts_information()
        existing_user = self.user_dao.get_all_user_information()
        if account.balance < 0:
            raise CustomExceptionMessage('Negative balance not allowed')
        for a in existing_user:
            if a.user_id == account.user_id:
                for b in existing_account:
                    if b.account_id == account.account_id:
                        return self.account_dao.update_account_information(account)
                    elif b is existing_account[-1]:
                        raise CustomExceptionMessage("Account to be updated not found")
            elif a is existing_user[-1]:
                raise CustomExceptionMessage("User ID not found")

    def service_withdraw_funds(self, account_id, amount: float):
        account_ob = self.service_get_account_information(account_id)
        if amount < 0:
            raise CustomExceptionMessage("Negative amount not allowed")
        account_ob.balance -= amount
        return self.service_update_account_information(account_ob)

    def service_deposit_funds(self, account_id, amount: float):
        account_ob = self.service_get_account_information(account_id)
        if amount < 0:
            raise CustomExceptionMessage("Negative amount not allowed")
        account_ob.balance += amount
        return self.service_update_account_information(account_ob)

    def service_transfer_fund_account(self, account_id: int, account_to_transfer_id, amount) -> list[Account]:
        sender = self.service_get_account_information(account_id)
        if sender.balance - amount < 0:
            raise CustomExceptionMessage("Insufficient funds")
        if amount < 0:
            raise CustomExceptionMessage("Negative amount not allowed")
        receiver = self.service_get_account_information(account_to_transfer_id)
        sender.balance -= amount
        receiver.balance += amount
        self.service_update_account_information(sender)
        self.service_update_account_information(receiver)
        return [receiver, sender]

    def service_delete_account_information(self, account_id: int) -> bool:
        existing_account = self.service_get_all_accounts_information()
        for a in existing_account:
            if a.account_id == account_id:
                return self.account_dao.delete_account_information(account_id)
        raise CustomExceptionMessage("Account to be deleted not found")
