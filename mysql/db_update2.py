# coding: utf-8
import os,sys
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import datetime
import pytz
import types
import time
from datetime import datetime

# update db
def db_update(cmd):
	db = MySQLdb.connect(host="localhost",
		user="root", passwd="root", db="learncenter",charset="utf8",port=3306)
	cursor = db.cursor()

	#  MySQL Execute
	cursor.execute(cmd)

	# Commit
	db.commit()

	print(cursor.rowcount, "record(s) affected")

	# close
	db.close()

if __name__ == "__main__":
	
	pwd = '1234'
	MemberID = '456'
	cmd = 'UPDATE member SET Password = "' + pwd + '" WHERE member.MemberID=' + MemberID
	db_update(cmd)
	
