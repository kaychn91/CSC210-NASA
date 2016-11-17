#!C:\Python27\python.exe


import cgitb
import cgi
import datetime
import hashlib
import MySQLdb as mdb
import sys
import json

def create_database():
    conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS csc210.Accounts(username varchar(30) primary key, password varchar(100), salt varchar(100), fName varchar(50), lName varchar(50), email varchar(100),dob date,gender char(1), favGame varchar(100)) ENGINE = InnoDB;") 
    conn.commit()
    conn.close()

	
def checkifexists(username):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	cmd = "SELECT * FROM Accounts WHERE username=%s"
	cursor.execute(cmd, (username,))
	results = cursor.fetchall()
	conn.close()
	if len(results)>0:
		return True
	else:
		return False


def insert_user(username,password,firstname,lastname,email,dob,gender,game):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	c = conn.cursor()
	currentdate = str(datetime.datetime.now())

	salt = currentdate
        hasher = hashlib.sha256()
        hasher.update(password)
        hasher.update(salt)
        encpaswd = hasher.hexdigest()
	
	cmd = "INSERT INTO Accounts VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
	c.execute(cmd,(username,encpaswd,currentdate,firstname,lastname,email,dob,gender,game))
	
	conn.commit()
	conn.close()

	
create_database()
	
cgitb.enable()

create_user = cgi.FieldStorage()

username = create_user['username'].value
password = create_user['password'].value
firstname = create_user['fName'].value
lastname = create_user['lName'].value
email = create_user['email'].value
dob = create_user['dob'].value
gender = create_user['gender'].value
game = create_user['game'].value
result = {}

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

if checkifexists(username):
	result['result'] = True
else:
	insert_user(username, password, firstname, lastname, email, dob, gender, game)
	result['result'] = False

sys.stdout.write(json.dumps(result, indent=1))
sys.stdout.write("\n")

sys.stdout.close()
