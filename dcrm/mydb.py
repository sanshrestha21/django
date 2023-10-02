import mysql.connector

database = mysql.connector.connect(
    host = "172.20.0.150",
    user = "gitea",
    passwd = "san977NP$$"
    )

# prepare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("create database elderco")

print("All Done!")

