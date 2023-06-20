from entities.Classroom import Classroom
from dotenv import load_dotenv
import traceback
import psycopg2
import os


class ClassroomDAO:
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


def getOneUser(id):
    user = None
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM usuario WHERE id = '{id}'")
        register = cursor.fetchone()
        if register:
            user = User(register[0], register[1], register[2], register[4], register[5])
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
        return user


def getAllUsers():
    users = []
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM usuario")
        registers = cursor.fetchall()
        for register in registers:
            users.append(User(register[0], register[1], register[2], register[4], register[5]))
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return users


def updateUser(id, newUser):
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE usuario SET name = %s, password = %s, ddd = %s, number = %s WHERE id = %s",
                       (newUser.name, newUser.password, newUser.ddd, newUser.number, id))

        connection.commit()
        if cursor.rowcount > 0:
            print("Success update!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()


def deleteUser(id):
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM usuario WHERE id= '{id}'")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success delete!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
