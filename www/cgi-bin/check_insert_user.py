#!C:\Python27\python.exe


import cgitb
import cgi
import datetime
import MySQLdb as mdb

def checkifexists(username):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM account WHERE username=%s', [username])
	results = cursor.fetchall()
	conn.close()
	if len(results)>0:
	 return True
	else:
	 return False

def insert_user(username,password,firstname,lastname,email,dob,gender,game):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	c = conn.cursor()
	c.execute("INSERT INTO account VALUES(%s,%s,%s,%s,%s,%s,%s,%s);",[username,password,firstname,lastname,email,dob,gender,game])
	
	conn.commit()
	conn.close()

cgitb.enable()

create_user = cgi.FieldStorage()
username = create_user['username'].value
print 'Content-Type: text/html'
print
print '''<html>
    <body>'''

username = create_user['username'].value
password = create_user['password'].value
firstname = create_user['fName'].value
lastname = create_user['lName'].value
email = create_user['email'].value
dob = create_user['dob'].value
gender = create_user['gender'].value
game = create_user['game'].value

if checkifexists(username):
	print '<h1> Username: ' + username + ' already exists! </h1>'
else:
	insert_user(username,password,firstname,lastname,email,dob,gender,game)
	print '<h1> User account created </h1>'
print '''
    </body>
</html>'''
