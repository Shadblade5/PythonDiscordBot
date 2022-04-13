import mysql.connector
import config

print("Starting connection to mySQL server with hostname: {0}".format(config.c.db_host))
mydb = mysql.connector.connect(
  host=config.c.db_host,
  user=config.c.db_username,
  password=config.c.db_password,
  database="pydiscordbot"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
