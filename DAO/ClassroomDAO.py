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
    success_operation = False
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        professor_id = classroom.professor if classroom.professor is not None else 'NULL'

        cursor.execute(f"INSERT INTO classroom (id, name, short_name, floor, type, professor_user_id) "
                       f"VALUES ('{classroom.id}', '{classroom.name}', '{classroom.short_name}', "
                       f"'{classroom.floor}', '{classroom.type}', {professor_id})")
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


def getOneClassroom(id):
    global cursor
    classroom = None
    try:
        connection = ClassroomDAO().openConnection()
        cursor = connection.cursor()
        query = """
                   SELECT
                    classroom.id,
                    classroom.name,
                    classroom.short_name,
                    classroom.floor,
                    classroom.type,
                    (select u.name from usuario as u
                     where u.id = classroom.professor_user_id) AS professor_responsavel,
                    CASE
                        WHEN occupancy.classroom_id IS NULL THEN 'avaliable'
                        ELSE 'occupied'
                    END AS status,
                    usuario.name AS user_name
                    FROM classroom
                    LEFT JOIN (
                        SELECT *
                        FROM occupancy
                        WHERE ending_date_time IS NULL
                    ) AS occupancy ON classroom.id = occupancy.classroom_id
                    LEFT JOIN usuario ON occupancy.user_id = usuario.id
                    WHERE classroom.id = %s
                """
        cursor.execute(query, (id,))
        register = cursor.fetchone()
        if register:
            classroom = Classroom(register[0], register[1], register[2], register[3],
                                  register[4], register[5], register[6], register[7])
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
        query = """
           SELECT
            classroom.id,
            classroom.name,
            classroom.short_name,
            classroom.floor,
            classroom.type,
            (select u.name from usuario as u
             where u.id = classroom.professor_user_id) AS professor_responsavel,
            CASE
                WHEN occupancy.classroom_id IS NULL THEN 'avaliable'
                ELSE 'occupied'
            END AS status,
            usuario.name AS user_name
            FROM classroom
            LEFT JOIN (
                SELECT *
                FROM occupancy
                WHERE ending_date_time IS NULL
            ) AS occupancy ON classroom.id = occupancy.classroom_id
            LEFT JOIN usuario ON occupancy.user_id = usuario.id
        """
        cursor.execute(query)
        registers = cursor.fetchall()
        for register in registers:
            classrooms.append(Classroom(register[0], register[1], register[2], register[3],
                                        register[4], register[5], register[6], register[7]))
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

