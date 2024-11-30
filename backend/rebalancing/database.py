import mysql.connector as MSQC
from mysql.connector import Error


class DatabaseConnectionManager:
    """
    This class is used to manage all the database connections
    """

    __connection = None

    @classmethod
    def get_connection(cls):
        """
        This function creates a connection to the database.
        """
        if cls.__connection is None:
            cls.__connection = MSQC.connect(
                host="localhost", database="cash_by_chance", user="root", password=""
            )

        return cls.__connection

    @classmethod
    def get_cursor(cls):
        """
        This function creates a cursor in order to execute queries.
        """
        return cls.get_connection().cursor()

    @classmethod
    def start_transaction(cls):
        """
        This function starts a transaction.
        """
        return cls.get_connection().start_transaction()

    @classmethod
    def commit_transaction(cls):
        """
        This function is used to commit transactions.
        """
        return cls.get_connection().commit()

    @classmethod
    def rollback_transaction(cls):
        """
        This function is used to rollback transactions.
        """
        return cls.get_connection().rollback()
