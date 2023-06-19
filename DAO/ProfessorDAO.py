from entities.Professor import Professor
from entities.User import User
from dotenv import load_dotenv
import traceback
import psycopg2
import os


class ProfessorDAO:
    def __init__(self):
        load_dotenv()  # Load the variables from .env file
        self.USER = os.getenv("USER")
        self.PASSWORD = os.getenv("PASSWORD")
        self.HOST = os.getenv("HOST")
        self.PORT = os.getenv("PORT")
        self.DATABASE = os.getenv("DATABASE")

    def openConnection(self):
        return psycopg2.connect(user=self.USER, password=self.PASSWORD,
                                host=self.HOST, port=self.PORT, database=self.DATABASE)


def insertProfessor(professor):
    try:
        connection = ProfessorDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO professor (user_id) "
                       f"VALUES ({professor.id})")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success insert!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()


def getOneProfessor(id):
    professor = None
    try:
        connection = ProfessorDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT u.id, u.name, u.ddd, u.number "
                       f"FROM professor AS p "
                       f"JOIN usuario AS u ON p.user_id = u.id "
                       f"WHERE p.user_id = {id};")
        register = cursor.fetchone()
        if register:
            professor = Professor(register[0], register[1], None, register[2], register[3])
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
        return professor


def getAllProfessors():
    professors = []
    try:
        connection = ProfessorDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT u.id, u.name, u.ddd, u.number "
                       f"FROM professor AS p "
                       f"JOIN usuario AS u ON p.user_id = u.id;")
        registers = cursor.fetchall()
        for register in registers:
            professors.append(Professor(register[0], register[1], None, register[2], register[3]))
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return professors


def deleteProfessor(id):
    try:
        connection = ProfessorDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM professor WHERE user_id= '{id}'")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success delete!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
