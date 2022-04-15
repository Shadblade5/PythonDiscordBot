import mysql.connector
import config

class DBClient:
  def __init__(self, db_host, db_username, db_password):
    self.client = mysql.connector.connect(host=db_host,
                                          user=db_username,
                                          password=db_password,
                                          database="pydiscordbot")
  def getUsers(self):
    mycursor = self.client.cursor()
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()
    return myresult



