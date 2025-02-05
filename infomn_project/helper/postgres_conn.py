import psycopg2
import pandas as pd
import json

class PostgresConnection:
    def __init__(self, host, database, user, password):
        """
        Initialize the PostgresConnection class with connection parameters.

        :param host: Hostname of the PostgreSQL server
        :param database: Name of the database
        :param user: Username to connect to the database
        :param password: Password to connect to the database
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        """
        Establish a connection to the PostgreSQL database.
        """
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connection to PostgreSQL DB successful")
        except Exception as e:
            print(f"Error: {e}")
            self.connection = None

    def query_db(self, query):
        """
        Execute a query and fetch results from the database.

        :param query: SQL query to be executed
        :return: Result of the query if successful, None otherwise
        """
        if self.connection is None:
            print("Connection not established")
            return None
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error: {e}")
            cursor.close()
            return None

    def write_db(self, query, data):
        """
        Execute a query and write data to the database.

        :param query: SQL query to be executed
        :param data: Data to be written to the database
        :return: True if the operation is successful, False otherwise
        """
        if self.connection is None:
            print("Connection not established")
            return False
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, data)
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            cursor.close()
            return False
        
    def write_dataframe(self, table_name, dataframe):
        """
        Write a pandas DataFrame to the database.

        :param table_name: Name of the table to write the data to
        :param dataframe: pandas DataFrame to be written to the database
        :return: True if the operation is successful, False otherwise
        """
        if self.connection is None:
            print("Connection not established")
            return False
        cursor = self.connection.cursor()
        try:
            for index, row in dataframe.iterrows():
                columns = ', '.join(row.index)
                values = ', '.join([f"'{str(val)}'" for val in row.values])
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
                cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            cursor.close()
            return False

    def write_csv(self, table_name, csv_file_path):
        """
        Write data from a CSV file to the database.

        :param table_name: Name of the table to write the data to
        :param csv_file_path: Path to the CSV file
        :return: True if the operation is successful, False otherwise
        """
        if self.connection is None:
            print("Connection not established")
            return False
        cursor = self.connection.cursor()
        try:
            dataframe = pd.read_csv(csv_file_path)
            for index, row in dataframe.iterrows():
                columns = ', '.join(row.index)
                values = ', '.join([f"'{str(val)}'" for val in row.values])
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
                cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            cursor.close()
            return False

    def write_json(self, table_name, json_file_path):
        """
        Write data from a JSON file to the database.

        :param table_name: Name of the table to write the data to
        :param json_file_path: Path to the JSON file
        :return: True if the operation is successful, False otherwise
        """
        if self.connection is None:
            print("Connection not established")
            return False
        cursor = self.connection.cursor()
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
            for row in data:
                columns = ', '.join(row.keys())
                values = ', '.join([f"'{str(val)}'" for val in row.values()])
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
                cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            cursor.close()
            return False

    def close(self):
        """
        Close the connection to the PostgreSQL database.
        """
        if self.connection:
            self.connection.close()
            print("Connection closed")