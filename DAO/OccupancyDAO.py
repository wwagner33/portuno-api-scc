from entities.Ocupancy import Occupancy
from dotenv import load_dotenv
import traceback
import psycopg2
import os


class OccupancyDAO:
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


def insertOccupancy(occupancy):
    success_operation = False
    try:
        connection = OccupancyDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO occupancy (goal, beginning_date_time, "
                       f"ending_date_time, semester_name, user_id, classroom_id, class_id) "
                       f"VALUES ('{occupancy.goal}', '{occupancy.beginning_time}', "
                       f"{occupancy.ending_time if occupancy.ending_time is not None else 'NULL'}, "
                       f"'{occupancy.semester}', {occupancy.user}, {occupancy.classroom}, "
                       f"{occupancy.the_class if occupancy.the_class is not None else 'NULL'})")
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


def getOneOccupancy(id):
    occupancy = None
    try:
        connection = OccupancyDAO().openConnection()
        cursor = connection.cursor()
        query = """
            SELECT
                occupancy.id, occupancy.beginning_date_time, occupancy.ending_date_time, occupancy.goal,
                classroom.name AS classroom_name,
                usuario.name AS user_name,
                semester.name AS semester_name,
                class.subject
            FROM occupancy
            JOIN usuario ON occupancy.user_id = usuario.id
            JOIN classroom ON occupancy.classroom_id = classroom.id
            JOIN semester ON occupancy.semester_name = semester.name
            LEFT JOIN class ON occupancy.class_id = class.id
            WHERE occupancy.id = %s
            """
        cursor.execute(query, id)
        register = cursor.fetchone()
        if register:
            occupancy = Occupancy(register[0], register[1], register[2], register[3],
                                  register[4], register[5], register[6], register[7])
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
        return occupancy


def getAllOccupancies():
    occupancies = []
    try:
        connection = OccupancyDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM occupancy")
        registers = cursor.fetchall()
        for register in registers:
            occupancy = Occupancy(register[0], register[1], register[2], register[3],
                                  register[4], register[5], register[6], register[7])
            occupancies.append(occupancy)
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return occupancies


def updateOccupancy(id, newOccupancy):
    success_operation = False
    try:
        connection = OccupancyDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE occupancy SET ending_date_time = %s WHERE id = %s",
                       (newOccupancy.ending_time, id))

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


def deleteOccupancy(id):
    success_operation = False
    try:
        connection = OccupancyDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM occupancy WHERE id= '{id}'")
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
