from custom_exceptions.custom_exception_message import CustomExceptionMessage
from data_access_layer.implementation_classes.user_postgres_dao import UserPostgresDao
from entities.users import User
from service_layer.implementation_services.user_service_imp import UserServiceImp

user_dao = UserPostgresDao()
user_service = UserServiceImp(user_dao)

user = User(0, "Test", "Test2")
user_update = User(100, "Update Test", "Update Test2")


def test_validate_create_user_method():
    try:
        user_service.service_create_user_entry(user)
    except CustomExceptionMessage as e:
        assert str(e) == "User ID not found"


def test_validate_get_user_information_method():
    try:
        user_service.service_get_user_information(100)
    except CustomExceptionMessage as e:
        assert str(e) == "User not found"


def test_validate_update_user_method():
    try:
        user_service.service_update_user_information(user_update)
    except CustomExceptionMessage as e:
        assert str(e) == "User to be updated not found"
