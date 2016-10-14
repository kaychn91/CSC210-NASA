#!C:\Python27\python.exe


import cgitb
import cgi
import datetime
import MySQLdb as mdb

def create_database():
    conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS csc210.Accounts(username varchar(30) primary key, password varchar(30),fName varchar(50), lName varchar(50), email varchar(100),dob date,gender char(1), favGame varchar(100)) ENGINE = InnoDB;") 
    conn.commit()
    conn.close()

	
def checkifexists(username):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Accounts WHERE username=%s', [username])
	results = cursor.fetchall()
	conn.close()
	if len(results)>0:
		return True
	else:
		return False


def insert_user(username,password,firstname,lastname,email,dob,gender,game):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	c = conn.cursor()
	c.execute("INSERT INTO Accounts VALUES(%s,%s,%s,%s,%s,%s,%s,%s);",[username,password,firstname,lastname,email,dob,gender,game])
	
	conn.commit()
	conn.close()

	
create_database()
	
cgitb.enable()

create_user = cgi.FieldStorage()
username = create_user['username'].value
print 'Content-Type: text/html'
print
print '''<html>
    <body>'''

username = create_user['username'].value
password = create_user['password'].value
pwdc = create_user['passwordC'].value
firstname = create_user['fName'].value
lastname = create_user['lName'].value
email = create_user['email'].value
dob = create_user['dob'].value
gender = create_user['gender'].value
game = create_user['game'].value

if checkifexists(username):
	print '<h1> Username: ' + username + ' already exists! </h1>'
else:
	if password == pwdc:
		insert_user(username,password,firstname,lastname,email,dob,gender,game)
		print '<h1> User account created </h1>'
        else:
                print '<h1> Your passwords don\'t match </h1>'

print '''
    </body>
</html>'''
