import mysql.connector

class ConexionBD:
    @staticmethod
    def conectarBD():
        return mysql.connector.connect(
                                    user='root', password=''
                                    ,host='localhost'
                                    ,database='jugueteria'
                                    ,port='3306'
                                    )