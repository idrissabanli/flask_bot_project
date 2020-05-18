import pymysql.cursors
from datetime import datetime


class QuestionsAnswers():
    def __init__(self):
        connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = '''CREATE TABLE if NOT EXISTS bot_project.questions_answers(
                            id int unsigned AUTO_INCREMENT PRIMARY KEY,
                            questions varchar(255) NOT NULL,
                            answers varchar(255) NOT NULL,
                            created_at datetime NOT NULL,
                            Index(id, questions)
                        );'''
                cursor.execute(sql)
        finally:
            connection.close()

    def all(self):
        connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        questions_answers = ''
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = 'SELECT * from bot_project.questions_answers;'
                cursor.execute(sql)
                questions_answers = cursor.fetchall()
        finally:
            connection.close()

        return questions_answers

    def create(self, questions, answers):
        connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = 'INSERT INTO bot_project.questions_answers(questions, answers, created_at) VALUE(%s, %s, %s)'

                cursor.execute(sql, (questions, answers, datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')))
                connection.commit()
        finally:
            connection.close()

    def update(self, id, questions, answers):
        connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = 'update  bot_project.questions_answers set questions=%s, answers=%s where id=%s;'

                cursor.execute(sql, (questions, answers, id))
                connection.commit()
        finally:
            connection.close()

    def delete(self, id):
        connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = 'delete from  bot_project.questions_answers  where id=%s;'
                cursor.execute(sql, (id,))
                connection.commit()
        finally:
            connection.close()


    def get(self, id):
        connection = pymysql.connect(host='localhost', user='root', password='123', db='bot_project', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        questions_answers = ''
        try:
            with connection.cursor() as cursor:
                
                # Create a new record
                sql = f'SELECT * from bot_project.questions_answers where id={id};'
                cursor.execute(sql)
                questions_answers = cursor.fetchone()
        finally:
            connection.close()

        return questions_answers


# 

# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()


