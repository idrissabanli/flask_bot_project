import pymysql.cursors
from datetime import datetime

def create_user_table():
    connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = '''CREATE TABLE if NOT EXISTS bot_project.users(
                        id int unsigned AUTO_INCREMENT PRIMARY KEY,
                        username varchar(30) NOT NULL,
                        email varchar(30) NOT NULL,
                        name varchar(30) NOT NULL,
                        surname varchar(30) NOT NULL,
                        password varchar(16) NOT NULL,
                        created_at datetime NOT NULL,
                        Index(id)
                    );'''
            cursor.execute(sql)
    finally:
        connection.close()

def create_user(username, email, name, surname, password):
    connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = 'INSERT INTO bot_project.users(username, email, name, surname, password, created_at) VALUE(%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (username, email, name, surname, password, datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')))
            connection.commit()
    finally:
        connection.close()



# class User():
#     def __init__(self):
#         connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
#         try:
#             with connection.cursor() as cursor:
#                 # Create a new record
#                 sql = '''CREATE TABLE if NOT EXISTS bot_project.users(
#                             id int unsigned AUTO_INCREMENT PRIMARY KEY,
#                             username varchar(30) NOT NULL,
#                             email varchar(30) NOT NULL,
#                             name varchar(30) NOT NULL,
#                             surname varchar(30) NOT NULL,
#                             password varchar(16) NOT NULL,
#                             created_at datetime NOT NULL,
#                             Index(id)
#                         );'''
#                 cursor.execute(sql)
#         finally:
#             connection.close()