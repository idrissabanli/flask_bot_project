class User():
    def __init__(self):
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