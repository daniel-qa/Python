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
import hashlib

'''
DATE : 2022/05/11
AUTHER: Daniel
'''
# query db
def db_query(cmd):
        db = MySQLdb.connect(host="localhost",
            user="root", passwd="root", db="learncenter",charset="utf8",port=3306)
        cursor = db.cursor()

        # .. MySQL ....
        cursor.execute(cmd)

        # ........
        result = cursor.fetchall()
        #print(result)

        #if(0):
        #       # ....
        #       for record in results:
        #               col1 = record[0]
        #               col2 = record[1]
        #       print( "%s, %s" % (col1, col2) )

        # close
        db.close()

        return result
      
# SHA1 Encode
def sha1_fun(data):

        #data = 't1'
        sha1 = hashlib.sha1(data.encode('utf-8')).hexdigest()
        #print(sha1)

        return sha1


if __name__ == "__main__":

        start = time.time()
        #print( "Start : %s" % start)

        # 測試連線
        if(0):
                # 查詢資料庫時間
                record = db_query("SELECT NOW();")
                print("目前資料庫的時間：", record)
        
        # Query Teacher data
        if(1):
                #cmd = "SELECT MemberID FROM member"  # All Data
                #cmd = "SELECT MemberID,LoginID,Password FROM member WHERE SchoolID BETWEEN 702 AND 712 OR SchoolID = 170 LIMIT 100"
                cmd = "SELECT MemberID,LoginID,Password FROM member WHERE SchoolID BETWEEN 702 AND 712 OR SchoolID = 170"

                ret = db_query(cmd)
                #print(len(ret))
                
                for dt in ret:
                        MemberID = str(dt[0])
                        print(MemberID)

                        # LoginID
                        LoginID =  str(dt[1])
                        print(LoginID)

                        # SHA1 Encode
                        pwdsha = sha1_fun(LoginID)
                        print(pwdsha)

                        # Change Teacher Password
                        cmd = 'UPDATE member SET Password = "' + pwdsha + '" WHERE member.MemberID=' + MemberID
                        db_update(cmd)
                        

        # Total Time
        end = time.time()
        elapsed = end - start
        m, s = divmod(elapsed, 60)
        h, m = divmod(m, 60)
        print( "Total Time: %d:%02d:%02d" % (h, m, s) )
