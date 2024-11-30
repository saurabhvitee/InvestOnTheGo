import os, json
import mysql.connector
from mysql.connector import Error

# read JSON file which is in the next parent folder
file = os.path.abspath('C:/Users/Kanishka/OneDrive/Desktop/code/DESIS/pyetf/env/Scripts') + "/data.json"
json_data=open(file).read()
json_obj = json.loads(json_data)


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val

# Function to Connect to database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Command to connect to database
connection = create_db_connection("localhost", "root", "Kanishka@8510070031", 'etfdatabase')
cursor = connection.cursor()


# parse json data to SQL insert
for i, item in enumerate(json_obj):
    symbol = validate_string(item.get("symbol", None))
    name = validate_string(item.get("name", None))
    url = validate_string(item.get("url", None))
    one_week_return = validate_string(item.get("one_week_return", None))
    one_year_return = validate_string(item.get("one_year_return", None))
    three_year_return = validate_string(item.get("three_year_return", None))
    five_year_return = validate_string(item.get("five_year_return", None))
    

    cursor.execute("INSERT INTO etfdata (symbol, name, url, one_week_return, one_year_return, three_year_return, five_year_return) VALUES (%s,	%s,	%s, %s, %s, %s, %s)", (symbol, name, url, one_week_return, one_year_return, three_year_return, five_year_return))
connection.commit()
connection.close()
