from psycopg import connect, OperationalError
import os


def create_connection():
    try:
        conn = connect(
            host=os.environ.get('host'),
            dbname=os.environ.get('database'),
            user=os.environ.get('user'),
            password=os.environ.get('password'),
            port=os.environ.get('port')
        )
        return conn
    except OperationalError as e:
        print([str(e)])


connection = create_connection()
