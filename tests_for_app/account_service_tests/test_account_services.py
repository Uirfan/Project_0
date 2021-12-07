from custom_exceptions.custom_exception_message import CustomExceptionMessage
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDao
from data_access_layer.implementation_classes.user_postgres_dao import UserPostgresDao
from entities.accounts import Account
from service_layer.implementation_services.account_service_imp import AccountServiceImp

account_dao = AccountPostgresDao()
user_dao = UserPostgresDao()
account_service = AccountServiceImp(account_dao, user_dao)

account = Account(0, "Test", 100, 100)
account_update = Account(2, "updateTest", 100, 200)


def test_validate_create_account_method():
    try:
        account_service.service_create_account_entry(account)
        assert False
    except CustomExceptionMessage as e:
        assert str(e) == "User ID not found"


def test_validate_get_account_information_method():
    try:
        account_service.service_get_account_information(100)
        assert False
    except CustomExceptionMessage as e:
        assert str(e) == "Account not found"

# def test_validate_get_all_account_information_method():
#     pass


def test_validate_update_account_method():
    try:
        account_service.service_update_account_information(account_update)
        assert False
    except CustomExceptionMessage as e:
        assert str(e) == "User ID not found" or str(e) == "Account to be updated not found"

def test_validate_transfer_funds_method():
    try:
        account_service.service_transfer_fund_account(3,2, 650)
        assert False
    except CustomExceptionMessage as e:
        assert str(e) == "Insufficient funds"
