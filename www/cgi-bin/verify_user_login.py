#!C:\Python27\python.exe


import cgitb
import cgi
import datetime
import json
import hashlib
import MySQLdb as mdb
import sys

	
def verifylogin(username, password):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	cmd = "SELECT password,salt FROM Accounts WHERE username=%s"
	cursor.execute(cmd, (username,))
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

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

if verifylogin(username,password):
	result['result']= True
else:
	result['result'] = False

sys.stdout.write(json.dumps(result, indent=1))
sys.stdout.write("\n")

sys.stdout.close()