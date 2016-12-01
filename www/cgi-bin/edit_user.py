#!C:\Python27\python.exe


import cgitb
import cgi
import datetime
import json
import hashlib
import MySQLdb as mdb
import sys


def change(username,password,firstname,lastname,email,gender,game):
    conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
    cursor = conn.cursor()
    cmd = "SELECT salt FROM Accounts WHERE username=%s"
    cursor.execute(cmd, (username,))
    result = cursor.fetchall()
    for row in result:
        salt = row[0]
        hasher = hashlib.sha256()
        hasher.update(password)
        hasher.update(salt)
        digest = hasher.hexdigest()
    cmd = """UPDATE Accounts
             SET password = %s,
                 fName = %s,
                 lName = %s,
                 email = %s,
                 gender = %s,
                 favGame = %s
             WHERE username = %s;"""
    data = (digest, firstname, lastname, email, gender, game, username)
    cursor.execute(cmd, data)
    conn.commit()
    conn.close()

def delete(username):
    conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
    cursor = conn.cursor()
    cmd= "DELETE FROM Accounts WHERE username=%s"
    cursor.execute(cmd, (username,))
    conn.commit()
    conn.close()

def getUser(username):
    conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
    c = conn.cursor()
    cmd = "SELECT password,fName,lName,email,dob,gender,favGame FROM Accounts WHERE username=%s" #getting encrypted password
    c.execute(cmd, (username,))
    results = c.fetchall()
    conn.close()
    if len(results)>0:
        return results
    else:
        return False

cgitb.enable()

verify_user = cgi.FieldStorage()
fnc = verify_user['fnc'].value
username = verify_user['username'].value

result= {}

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

if fnc == 'delete':
    delete(username)
    result['result'] = True
elif fnc == 'change':
    password = verify_user['password'].value
    firstname = verify_user['fName'].value
    lastname = verify_user['lName'].value
    email = verify_user['email'].value
    gender = verify_user['gender'].value
    game = verify_user['game'].value
    change(username,password,firstname,lastname,email,gender,game)
    result['result'] = True
elif fnc == 'getUser':  # still doesn't work
    result['result'] = getUser(username)
else:
	pass

sys.stdout.write(json.dumps(result, indent=1))
sys.stdout.write("\n")

sys.stdout.close()
