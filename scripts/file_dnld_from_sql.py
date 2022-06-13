
import mysql.connector as connection
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv('../env/.env')

host = os.environ.get("host")
username = os.environ.get("username")
password = os.environ.get("password")
port = os.environ.get("port")
database = os.environ.get("database")
query = "SELECT * FROM colas_sharing.form_display;"
try:
    mydb = connection.connect(
        host=host, database=database, user=username, passwd=password, use_pure=True)
    result_dataFrame = pd.read_sql(query, mydb)
    mydb.close()  # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

# result_dataFrame = pd.read_sql(query, mydb)


result_dataFrame.head()


result_dataFrame.to_csv('data/colas_sharing.form_display.csv')


result_dataFrame.to_excel('data/colas_sharing_form_display.xlsx')
