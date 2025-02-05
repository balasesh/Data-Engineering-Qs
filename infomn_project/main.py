from helper.postgres_conn import PostgresConnection

POSTGRES_HOST = 'localhost'
POSTGRES_USER = 'username'
POSTGRES_PASSWORD = 'password'
POSTGRES_DATABASE = 'infomn_db'

def main():
    # Step 1 - Access the data 
    # load th CSV file
    # Step 2 - Process the data
    # Using pandas create a dataframe
    # Step 3 - Load th edata into DB
    conn = PostgresConnection(host, database, user, password)
    conn.connect()
    conn.close()