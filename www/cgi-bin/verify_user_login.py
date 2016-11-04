#!C:\Python27\python.exe


import cgitb
import cgi
import datetime
import json
import hashlib
import MySQLdb as mdb

	
def verifylogin(username, password):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	cursor.execute('SELECT password,salt FROM Accounts WHERE username=%s', [username])
	result = cursor.fetchall()
	for row in result:
		encrypted = row[0]
		salt = row[1]
		hasher = hashlib.sha256()
		hasher.update(password)
		hasher.update(salt)
		digest = hasher.hexdigest()

	conn.close()
	
	if digest == encrypted:
		return True
	else:
		return False


cgitb.enable()

verify_user = cgi.FieldStorage()
username = verify_user['username'].value
password = verify_user['password'].value
result= {}
print 'Content-Type: text/html'
print
print '''<html>
	<body>'''

if verifylogin(username,password):
	result['result']= True
	json.dumps(result)

else:
	result['result'] = False
	json.dumps('result')
	