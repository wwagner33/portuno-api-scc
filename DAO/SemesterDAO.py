from entities.Semester import Semester
from datetime import datetime
from dotenv import load_dotenv
import traceback
import psycopg2
import os


class SemesterDAO:
    def __init__(self):
        load_dotenv()
        self.USER = os.getenv("USER")
        self.PASSWORD = os.getenv("PASSWORD")
        self.HOST = os.getenv("HOST")
        self.PORT = os.getenv("PORT")
        self.DATABASE = os.getenv("DATABASE")

    def openConnection(self):
        return psycopg2.connect(user=self.USER, password=self.PASSWORD,
                                host=self.HOST, port=self.PORT, database=self.DATABASE)


def insertSemester(semester):
    try:
        connection = SemesterDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO semester (name, beginning_date, ending_date) "
                       f"VALUES ('{semester.name}', '{semester.beginning_date}', '{semester.ending_date}')")
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

        cursor.execute(f"UPDATE semester SET name = '{newSemester.name}', "
                       f"beginning_date = '{newSemester.beginning_date}', "
                       f"ending_date = '{newSemester.ending_date}' "
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
