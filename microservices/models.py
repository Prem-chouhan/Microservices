import sys
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from connect import db_connection
import os
# import socket

my_db = db_connection()


class DbManaged:

    def __init__(self):
        pass

    def insert_register(self, data):
        """Insert Query is fired Here and registration is done"""
        sql = "INSERT INTO user(email,password,confirm_password) VALUES (%s, %s, %s)"
        val = (data['email'], data['password'], data['confirm_password'])
        my_db.queryExecute(sql, val)

    def read_email(self, email=None, id=None):
        id = None
        """Select Query is fired Here and email address is present or not is shown """
        sql = "SELECT email,id FROM user where email = '" + email + "'"
        result = my_db.queryfetch(sql)
        print(result)
        email, id = result[0]
        print(email, id)
        if id is not None:
            return id, email
        else:
            return None

    def update_password(self, data, key):
        """Here password is updated with update query"""
        sql = "UPDATE user SET password = '" + data['password'] + "' WHERE email = '" + key + "' "
        my_db.query(sql)
