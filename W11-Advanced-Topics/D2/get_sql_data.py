import pandas as pd
import numpy as np
from getpass import getpass
import pymysql
import requests
import time
import warnings

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
warnings.filterwarnings('ignore')

def create_connection():
    """
    Create a connection to a MySQL database.
    Prompts the user for the database password and lists available databases.
    
    Returns:
        cnx: pymysql.connections.Connection object
            The connection object to the MySQL database.
    """
    password = getpass("Please, kindly insert your password: ")
    cnx = pymysql.connect(user='root', password=password, host='localhost')
    
    if cnx.open:
        print("Connection successfully opened.")
        print()
        cursor = cnx.cursor()
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("Available databases:")
        db_list = [db[0] for db in databases]
        for db in db_list:
            print(f"- {db}")
        print()
    else:
        print("Failed to open connection.")
        print()
        return None
    
    while True:
        database = input("Please, kindly insert your database name: ")
        if database in db_list:
            cnx.select_db(database)
            break
        else:
            print("Invalid database name. Please choose from the available databases.")
            print()
    
    return cnx

def save_data(df):
    file_format = input("Please enter either 'excel' or 'csv': ").strip().lower()
    print()

    if file_format == 'excel':
        file_name = input("Please enter the file name (without extension): ") + '.xlsx'
        df.to_excel(file_name, index=False)
        print(f"Data successfully saved as {file_name}.")
        print()
    elif file_format == 'csv':
        file_name = input("Please enter the file name (without extension): ") + '.csv'
        df.to_csv(file_name, index=False)
        print(f"Data successfully saved as {file_name}.")
        print()
    else:
        print("Invalid format. Please enter either 'excel' or 'csv'.")
        print()

connection = create_connection()

if connection:
    while True:
        query = input("Please enter your SQL query or command (or 'exit' to quit): ")
        print()
        if query.lower() == 'exit':
            connection.close()
            print("Connection closed.")
            break
        try:
            df = pd.read_sql(query, connection)
            print("Query executed successfully. Here is the data:")
            print()
            print(df)
            print()
            prompt = input("Do you want to save the data? (yes/no): ").strip().lower()
            print()
            if prompt == 'yes':
                save_data(df)
        except Exception as e:
            print(f"Error: {e}")
            print("Try again.")
            print()