from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDao
from entities.accounts import Account

account_dao = AccountPostgresDao()
account = Account(0, "Test", 1, 100)



def test_create_account_success():
    created_account = account_dao.create_account_entry(account)
    assert created_account.account_id != 0


def test_get_account_success():
    got_account = account_dao.get_account_information(3)
    assert got_account.account_id != 0 and got_account.account_name != ""


def test_get_all_account_success():
    accounts = account_dao.get_all_account_information()
    assert len(accounts) > 2



def test_update_account_success():
    update_account = Account(25, 'Updated Test', 15, 111)
    updated_account = account_dao.update_account_information(update_account)
    assert updated_account.account_name == "Updated Test"


def test_delete_account_success():
    result = account_dao.delete_account_information(15)
    assert result
