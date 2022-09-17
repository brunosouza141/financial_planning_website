import mysql.connector
import datetime
import dotenv
dotenv.load_dotenv()

connection = mysql.connector.connect(
  host="localhost",
  user="DB_CONNECTION_USER",
  password="DB_CONNECTION_PASSWORD",
  database="db_user_data"
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

userid = cursor.lastrowid

cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID:", userid)