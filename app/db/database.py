import pymysql

class Database:
    """Handles database connection and raw SQL execution."""

    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="main",
            database="task_manager",
            cursorclass=pymysql.cursors.DictCursor
        )

    def execute(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor.fetchall()
