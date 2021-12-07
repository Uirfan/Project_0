from data_access_layer.abstract_classes.user_dao import UserDAO
from entities.users import User
from util.database_connection import connection


class UserPostgresDao(UserDAO):
    def create_user_entry(self, user: User) -> User:
        sql = "insert into users values(default, %s, %s) returning user_id"
        cursor = connection.cursor()
        cursor.execute(sql, (user.first_name, user.last_name))
        connection.commit()
        user_id = cursor.fetchone()[0]
        user.user_id = user_id
        return user

    def get_user_information(self, user_id: int) -> User:
        sql = "select * from users where user_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        user_record = cursor.fetchone()
        user_ob = User(*user_record)
        return user_ob

    def get_all_user_information(self) -> list[User]:
        sql = "select * from users"
        cursor = connection.cursor()
        cursor.execute(sql)
        user_record = cursor.fetchall()
        user_list = []
        for a in user_record:
            user_ob = User(*a)
            user_list.append(user_ob)
        return user_list

    def update_user_information(self, user: User) -> User:
        sql = "update users set first_name = %s, last_name = %s where user_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (user.first_name, user.last_name, user.user_id))
        connection.commit()
        return user

    def delete_user_information(self, user_id: int) -> bool:
        sql = "delete from users where user_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()
        return True
