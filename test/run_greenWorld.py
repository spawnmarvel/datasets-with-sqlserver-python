import pyodbc 

# https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15
import random
import datetime

server = r"localhost\sqlexpress"
database = "TestGreenWorld" 
username = "misp" 
password = "astring6r473"
cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE="+database+";UID="+username+";PWD="+ password)
cursor = cnxn.cursor()


def get_version():
    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        row = cursor.fetchone()


def get_pump():
    cursor.execute("SELECT * FROM test.pump;") 
    row = cursor.fetchall() 
    print(row)

def insert_pump():
    ran_number = random.randint(20,150)
    current_time_utc = datetime.datetime.utcnow()
    current_time_utc.strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""INSERT INTO test.pump (p_name, p_plant) VALUES (?,?)""", "P3","EAR") 
    cnxn.commit()

# print(get_version())
# insert_pump()
print(get_pump())




