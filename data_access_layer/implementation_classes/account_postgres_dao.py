from data_access_layer.abstract_classes.account_dao import AccountDAO
from entities.accounts import Account
from util.database_connection import connection


class AccountPostgresDao(AccountDAO):
    def create_account_entry(self, account: Account) -> Account:
        sql = "insert into accounts values(default, %s, %s,%s) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_name, account.user_id, account.balance))
        connection.commit()
        account_id = cursor.fetchone()[0]
        account.account_id = account_id
        return account

    def get_account_information(self, account_id: int) -> Account:
        sql = "select * from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_record = cursor.fetchone()
        accountob = Account(*account_record)
        return accountob

    def get_all_account_information(self) -> list[Account]:
        sql = "select * from accounts"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_record = cursor.fetchall()
        account_list = []
        for a in account_record:
            account_ob = Account(*a)
            account_list.append(account_ob)
        return account_list

    def update_account_information(self, account: Account) -> Account:
        sql = "update accounts set account_name = %s, user_id = %s, balance = %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_name, account.user_id, account.balance, account.account_id))
        connection.commit()
        return account

    def delete_account_information(self, account_id: int) -> bool:
        sql = "delete from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True
