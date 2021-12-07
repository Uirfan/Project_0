from data_access_layer.implementation_classes.user_postgres_dao import UserPostgresDao
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDao
from entities.users import User
from service_layer.abstract_services.user_service import UserService
from custom_exceptions.custom_exception_message import CustomExceptionMessage


class UserServiceImp(UserService):
    def __init__(self, user_dao, account_dao):
        self.user_dao: UserPostgresDao = user_dao
        self.account_dao: AccountPostgresDao = account_dao

    def service_create_user_entry(self, user: User) -> User:
        return self.user_dao.create_user_entry(user)

    def service_get_user_information(self, user_id: int) -> User:
        existing_user = self.service_get_all_users_information()
        for a in existing_user:
            if a.user_id == user_id:
                return self.user_dao.get_user_information(user_id)
        raise CustomExceptionMessage("User not found")

    def service_get_all_users_information(self) -> list[User]:
        return self.user_dao.get_all_user_information()

    def service_update_user_information(self, user: User) -> User:
        existing_user = self.service_get_all_users_information()
        for a in existing_user:
            if a.user_id == user.user_id:
                return self.user_dao.update_user_information(user)
        raise CustomExceptionMessage("User to be updated not found")

    def service_delete_user_information(self, user_id: int) -> bool:
        existing_users = self.service_get_all_users_information()
        existing_accounts = self.account_dao.get_all_account_information()
        for a in existing_users:
            if a.user_id == user_id:
                for b in existing_accounts:
                    if b.user_id == user_id:
                        raise CustomExceptionMessage("Before deleting user, please delete associated accounts")
                    else:
                        return self.user_dao.delete_user_information(user_id)
        raise CustomExceptionMessage("User to be deleted not found")
