from data_access_layer.implementation_classes.user_postgres_dao import UserPostgresDao
from entities.users import User

user_dao = UserPostgresDao()
user = User(0, "Test", "Test2")

user_id_db = 0


def test_create_user_success():
    global user_id_db
    created_user = user_dao.create_user_entry(user)
    user_id_db = created_user.user_id
    assert created_user.user_id != 0


def test_get_user_success():
    got_user = user_dao.get_user_information(2)
    assert got_user.user_id != 0 and got_user.first_name != ""


def test_get_all_user_success():
    users = user_dao.get_all_user_information()
    assert len(users) > 1

def test_update_user_success():
    update_user = User(1, 'Updated Test', 'Updated Test2')
    updated_user = user_dao.update_user_information(update_user)
    assert updated_user.first_name == "Updated Test"


def test_delete_user_success():
    result = user_dao.delete_user_information(2)
    assert result
