####################################
# File name: connection.py         #
# Description:
# Author: Team-13                  #
# Submission: Spring-2019          #
# Instructor: Dragutin Petkovic    #
####################################
import mysql.connector

conn = mysql.connector.connect(host="",
                               database='',
                               user='',
                               password='',
                               auth_plugin='mysql_native_password')
cursor = conn.cursor()

#
# conn = mysql.connector.connect(host = "localhost",
#                             database = 'CSC648',
#                             user = 'root',
#                             password = 'Derectorjin1',
#                             auth_plugin='mysql_native_password')
# cursor = conn.cursor()
