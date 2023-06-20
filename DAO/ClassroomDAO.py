from entities.Classroom import Classroom
from dotenv import load_dotenv
import traceback
import psycopg2
import os


class ClassroomDAO:
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


def insertClassroom(classroom):
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO classroom (id, name, short_name, floor,  type) "
                       f"VALUES ('{classroom.id}', '{classroom.name}', '{classroom.short_name}',"
                       f" '{classroom.floor}', '{classroom.type}')")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success insert!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()


def getOneClassroom(id):
    global cursor
    classroom = None
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM classroom WHERE id = '{id}'")
        register = cursor.fetchone()
        if register:
            classroom = Classroom(register[0], register[1], register[2], register[3], register[4])
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
        return classroom


def getAllClassrooms():
    classrooms = []
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM classroom")
        registers = cursor.fetchall()
        for register in registers:
            classrooms.append(Classroom(register[0], register[1], register[2], register[3], register[4]))
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return classrooms


def updateClassroom(id, newClassroom):
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE classroom SET name = %s, short_name = %s, floor = %s, type = %s WHERE id = %s",
                       (newClassroom.name, newClassroom.short_name, newClassroom.floor, newClassroom.type, id))

        connection.commit()
        if cursor.rowcount > 0:
            print("Success update!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

def updateProfessor_user_id(id, professor_user_id):
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE classroom SET professor_user_id = %s WHERE id = %s",
                       (professor_user_id, id))
        connection.commit()
        if cursor.rowcount > 0:
            print("Success update professor id!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

def deleteClassroom(id):
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM classroom WHERE id= '{id}'")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success delete!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

