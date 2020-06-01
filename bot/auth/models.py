import pymysql.cursors
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash 

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
                        password varchar(255) NOT NULL,
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
            password = generate_password_hash(password)
            sql = 'INSERT INTO bot_project.users(username, email, name, surname, password, created_at) VALUE(%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (username, email, name, surname, password, datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')))
            connection.commit()
    finally:
        connection.close()

def check_user_exists(username, password):
    connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    founded_user = None
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = 'select * from bot_project.users where username=%s;'
            cursor.execute(sql, (username, ))
            connection.commit()
            user = cursor.fetchone()
            if user:
                user_pw_hashed = user['password']
                if check_password_hash(user_pw_hashed, password):
                    founded_user = user
    finally:
        connection.close()
    return founded_user


def check_username_model(username):
    connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    user_founded = False
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = 'select * from bot_project.users where username=%s;'
            cursor.execute(sql, (username,))
            connection.commit()
            user = cursor.fetchone()
            if user:
                user_founded = True
    finally:
        connection.close()
    return user_founded


def check_email_model(email):
    connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    user_founded = False
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = 'select * from bot_project.users where email=%s;'
            cursor.execute(sql, (email,))
            connection.commit()
            user = cursor.fetchone()
            if user:
                user_founded = True
    finally:
        connection.close()
    return user_founded


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