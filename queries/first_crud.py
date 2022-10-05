from mysql import connector
import pymysql
import datetime
import os
import dotenv
dotenv.load_dotenv()
connection = pymysql.Connect(
  host="localhost",
  user= os.getenv("DB_CONNECTION_USER"),
  password= os.getenv("DB_CONNECTION_PASSWORD"),
  database="db_user_data",
)

cursor = connection.cursor()

#sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
#data = (
#  'Primeiro Usuário',
#  'primeirousuario@teste.com.br',
#  datetime.datetime.today()
#)

#cursor.execute(sql, data)
#connection.commit()


cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID:")