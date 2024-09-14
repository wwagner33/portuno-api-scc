# Teste de conexão com o Supabase e acesso ao banco, usando variáveis presentes no ENV

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
user = os.getenv("USER")
passwd = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")
database = os.getenv("DATABASE")

print(user, passwd, host, port, database)
connection = psycopg2.connect(user=user, password=passwd, host=host, port=port, database=database)
cursor = connection.cursor()
cursor.execute("SELECT * FROM class")
result = cursor.fetchall()
print(result)