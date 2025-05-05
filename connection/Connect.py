from peewee import *
def connect():
    mysql_db = MySQLDatabase('SHnD1234_123',
                             user='SHnD1234_321',
                             password='753753',
                             host='10.11.13.118',
                             port=3306)
    return mysql_db

if __name__ == "__main__":
    connect().connect()