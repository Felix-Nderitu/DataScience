import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Bot_Guru.inc2023",
  database = "DatabaseTwo"
)


mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE DatabaseTwo")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)
#print("Connection")

#Write the table
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#To show the tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
#Using the primary key
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

print(mycursor.rowcount, "record inserted.")