import mysql.connector


class DB_instance():
    __instance = None
    __db_connection = None

    DB_NAME = "BooksDB"

    @staticmethod
    def instance():
        if DB_instance.__instance is None:
            DB_instance.__instance = DB_instance()
        return DB_instance.__instance

    def __init__(self):
        self.__db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="1458"
        )

    def get_cursor(self):
        if self.__db_connection:
            return self.__db_connection.cursor()
        return None

    def set_db(self):
        cursor = self.__db_connection.cursor()

        try:
            cursor.execute("USE {};".format(self.DB_NAME))
        except mysql.connector.Error as err:
            print("Failed to set db {}".format(err))

    def commit(self):
        if self.__db_connection:
            self.__db_connection.commit()


def create_db(writer, book):
    instance = DB_instance.instance()
    cursor = instance.get_cursor()

    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(instance.DB_NAME))
        instance.set_db()
        # create tables here
        cursor.execute(writer)
        cursor.execute(book)
    except mysql.connector.Error as err:
        print("Failed to create db {}".format(err))


def get_data(query):
    instance = DB_instance.instance()
    cursor = instance.get_cursor()
    try:
        instance.set_db()
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [x[0] for x in cursor.description]

        data = []
        for result in rows:
            row = {}
            idx = 0
            for header in headers:
                row[header] = result[idx]
                idx += 1
            data.append(row)
        return data
    except mysql.connector.Error as err:
        print("Failed to fetch data: {}".format(err))


def execute_command(query):
    instance = DB_instance.instance()
    cursor = instance.get_cursor()

    try:
        instance.set_db()
        cursor.execute(query)
        instance.commit()
    except mysql.connector.Error as err:
        print("Failed to insert/update data {}".format(err))
