from entities.Semester import Semester
from datetime import datetime
import psycopg2
import traceback

class SemesterDAO:
    def __init__(self):
        self.USER = "postgres"
        self.PASSWORD = "Jv4984538171"
        self.HOST = "127.0.0.1"
        self.PORT = "5432"
        self.DATABASE = "portuno"

    def openConnection(self):
        return psycopg2.connect(user=self.USER, password=self.PASSWORD,
                                host=self.HOST, port=self.PORT, database=self.DATABASE)

def insertSemester(semester):
    try:
        connection = SemesterDAO().openConnection()
        cursor = connection.cursor()

        beginning_date = datetime.strptime(semester.beginning_date, '%d/%m/%Y')
        ending_date = datetime.strptime(semester.ending_date, '%d/%m/%Y')

        cursor.execute(f"INSERT INTO semester (name, beginning_date, ending_date) "
                       f"VALUES ('{semester.name}', '{beginning_date}', '{ending_date}')")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success insert!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

def getOneSemester(name):
    semester = None  # Inicializa a variável semester antes do bloco try
    try:
        connection = SemesterDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM semester WHERE name = '{name}'")
        register = cursor.fetchone()
        if register:
            semester = Semester(register[0], register[1], register[2])
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
        return semester

def getAllSemesters():
    semesters = []
    try:
        connection = SemesterDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM semester")
        registers = cursor.fetchall()
        print(registers)
        for register in registers:
            semesters.append(Semester(register[0], register[1], register[2]))

    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return registers

def updateSemester(name, newSemester):
    try:
        connection = SemesterDAO().openConnection()
        cursor = connection.cursor()

        beginning_date = datetime.strptime(newSemester.beginning_date, '%d/%m/%Y')
        ending_date = datetime.strptime(newSemester.ending_date, '%d/%m/%Y')

        cursor.execute(f"UPDATE semester SET name = '{newSemester.name}', "
                       f"beginning_date = '{beginning_date}', "
                       f"ending_date = '{ending_date}' "
                       f"WHERE name = '{name}'")

        connection.commit()
        if cursor.rowcount > 0:
            print("Success update!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

def deleteSemester(name):
    try:
        connection = SemesterDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM semester WHERE name= '{name}'")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success delete!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()



