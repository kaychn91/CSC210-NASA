#!C:\Python27\python.exe

import cgitb
import cgi
import datetime
import hashlib
import MySQLdb as mdb

def authenticate(username, password):
    conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	result = cursor.execute('SELECT * FROM Accounts WHERE username=%s', [username])
	if results.rowcount == 1: 
        row = results.next()
        encrypted = row[1]
        salt = row[2]

        hasher = hashlib.sha256()
        hasher.update(password)
        hasher.update(salt)

        digest = hasher.hexdigest()

        conn.close()

        return digest == encrypted
    else:
        return False


cgitb.enable()
user_info = cgi.FieldStorage()
username = user_info['username'].value
password = user_info['password'].value


        
if authenticate(username, password):
    # successfully logged in
else:
    # failed to log in