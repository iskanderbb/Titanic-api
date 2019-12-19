import connexion
import six
import pymysql
from swagger_server.app import app
from swagger_server.db_config import mysql
from flask import jsonify
from flask import flash, request

from swagger_server.models.people import People  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.person_data import PersonData  # noqa: E501
from swagger_server import util

def people_add(person):  # noqa: E501
                try:
                        if connexion.request.is_json:
                            person = PersonData.from_dict(connexion.request.get_json())  # noqa: E501
                            
                            sql = "INSERT INTO passengers(survived, passengerClass, name, sex, age, siblingsOrSpousesAboard, parentsOrChildrenAboard, fare) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                            datap = (person.survived, person.passenger_class, person.name, person.sex, person.age, person.siblings_or_spouses_aboard, person.parents_or_children_aboard, person.fare)
                            conn = mysql.connect()
                            cursor = conn.cursor()
                            cursor.execute(sql, datap)
                            conn.commit()
                            resp = jsonify('User added successfully!')
                            resp.status_code = 200
                            return resp
                        else:
                            return not_found()
                except Exception as e:
                        print(e)
                finally:
                        cursor.close() 
                        conn.close()
def people_list():  # noqa: E501
                try:
                        conn = mysql.connect()
                        cursor = conn.cursor(pymysql.cursors.DictCursor)
                        cursor.execute("SELECT * FROM passengers")
                        rows = cursor.fetchall()
                        resp = jsonify(rows)
                        resp.status_code = 200
                        return resp
                except Exception as e:
                        print(e)
                finally:
                        cursor.close() 
                        conn.close()

def person_delete(uuid):  # noqa: E501
            try:
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passengers WHERE id=%s", uuid)
                conn.commit()
                resp = jsonify('User deleted successfully!')
                resp.status_code = 200
                return resp
            except Exception as e:
                print(e)
            finally:
                cursor.close() 
                conn.close()


def person_get(uuid):  # noqa: E501
            try:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute("SELECT * FROM passengers WHERE id=%s", uuid)
                row = cursor.fetchone()
                resp = jsonify(row)
                resp.status_code = 200
                return resp
            except Exception as e:
                print(e)
            finally:
                cursor.close() 
                conn.close()


def person_update(uuid, person):  # noqa: E501
        try:
            if connexion.request.is_json:
               person = PersonData.from_dict(connexion.request.get_json())  # noqa: E501
           
               sql = "update passengers set survived=%s, passengerClass=%s, name=%s, sex=%s, age=%s, siblingsOrSpousesAboard=%s, parentsOrChildrenAboard=%s, fare=%s where id=%s"
               datap = (person.survived, person.passenger_class, person.name, person.sex, person.age, person.siblings_or_spouses_aboard, person.parents_or_children_aboard, person.fare,uuid)
               conn = mysql.connect()
               cursor = conn.cursor()
               cursor.execute(sql, datap)
               conn.commit()
               resp = jsonify('User updated successfully!')
               resp.status_code = 200
               return resp             
            else:
                return not_found()
        except Exception as e:
                print(e)
        finally:
                cursor.close() 
                conn.close()

