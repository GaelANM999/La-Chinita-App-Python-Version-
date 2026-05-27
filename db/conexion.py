import pymysql

class ConexionBD:
    @staticmethod
    def conectarBD():
        return pymysql.connect(
            user='root',
            password='',
            host='localhost',
            database='jugueteria',
            port=3306,
            cursorclass=pymysql.cursors.DictCursor
        )