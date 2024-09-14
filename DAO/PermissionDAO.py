from entities.Ocupancy import Occupancy
from dotenv import load_dotenv
import traceback
import psycopg2
import os

from entities.Permission import Permission


class PermissionDAO:
    def __init__(self):
        load_dotenv()
        self.USER = os.getenv("USER")
        self.PASSWORD = os.getenv("PASSWORD")
        self.HOST = os.getenv("HOST")
        self.PORT = os.getenv("PORT")
        self.DATABASE = os.getenv("DATABASE")

    def openConnection(self):
        return psycopg2.connect(user=self.USER, password=self.PASSWORD,
                                host=self.HOST, port=self.PORT, DATABASE=self.DATABASE)


def insertPermission(permission):
    success_operation = False
    try:
        connection = PermissionDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO permission (beginning_date_time, "
                       f"ending_date_time, professor_user_id, user_id, classroom_id ) "
                       f"VALUES ('{permission.beginning_time}', '{permission.ending_time}', "
                       f"{permission.professor}, {permission.user}, {permission.classroom})")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success insert!")
            success_operation = True
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return success_operation


def getOnePermission(id):
    permission = None
    try:
        connection = PermissionDAO().openConnection()
        cursor = connection.cursor()
        query = """
             SELECT
                permission.id, 
                permission.beginning_date_time, 
                permission.ending_date_time,
                (SELECT usuario.name FROM usuario WHERE usuario.id = professor.user_id) AS professor_name,
                usuario.name AS user_name,
                classroom.name AS classroom_name
            FROM permission
            JOIN professor ON permission.professor_user_id = professor.user_id
            JOIN usuario ON permission.user_id = usuario.id
            JOIN classroom ON permission.classroom_id = classroom.id
            WHERE permission.id = %s
            """
        cursor.execute(query, (id,))
        register = cursor.fetchone()
        if register:
            permission = Permission(register[0], register[1], register[2], register[3], register[4], register[5])
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
        return permission


def getAllPermissions():
    permissions = []
    try:
        connection = PermissionDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM permission")
        registers = cursor.fetchall()
        for register in registers:
            permission = Permission(register[0], register[1], register[2], register[3], register[4], register[5])
            permissions.append(permission)
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return permissions


def updatePermission(id, ending_date_time):
    success_operation = False
    try:
        connection = PermissionDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE permission SET ending_date_time = %s WHERE id = %s",
                       (ending_date_time, id))

        connection.commit()
        if cursor.rowcount > 0:
            print("Success update!")
            success_operation = True
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return success_operation


def deletePermission(id):
    success_operation = False
    try:
        connection = PermissionDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM permission WHERE id= '{id}'")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success delete!")
            success_operation = True
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return success_operation
