#!/usr/bin/env python

import cgitb
import cgi
import psycopg2
import hashlib
import datetime


def create_database():
    conn = psycopg2.connect('accounts.db')
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS accounts')

    c.execute('CREATE TABLE IF NOT EXISTS accounts(username varchar(30) primary key, password varchar(30),'
              'salt varchar(100), fName varchar(50), lName varchar(50), email varchar(100),dob date,'
              'gender char(1), favGame varchar(100)')

    conn.commit()
    conn.close()


def user_exists(username):
    conn = psycopg2.connect('accounts.db')
    c = conn.cursor()
    results = c.execute('SELECT * FROM accounts WHERE username=?', [username])
    if results.arraysize == 1:
        return True
    else:
        return False


def insert_user(username, password, fname, lname, email, dob, gender, favgame):
    conn = psycopg2.connect('accounts.db')
    c = conn.cursor()

    salt = str(datetime.datetime.now())

    hasher = hashlib.sha256()
    hasher.update(password)
    hasher.update(salt)
    encrypted = hasher.hexdigest()

    c.execute('INSERT INTO accounts VALUES(?,?,?,?,?,?,?,?,?);', [username, encrypted, salt, fname, lname,
                                                                  email, dob, gender, favgame])
    print '<h1> User account created </h1>'
    conn.commit()
    conn.close()


def print_users():
    conn = psycopg2.connect('accounts.db')
    c = conn.cursor()

    for row in c.execute('SELECT * FROM accounts'):
        print row


cgitb.enable()

user_info = cgi.FieldStorage()

u = user_info['username'].value
pwd = user_info['password'].value
pwdc = user_info['passwordC'].value
fn = user_info['fName'].value
ln = user_info['lName'].value
eml = user_info['email'].value
bd = user_info['dob'].value
gen = user_info['gender'].value
game = user_info['game'].value

print 'Content-Type: text/html'
print
print '''<html>
<body>'''

if user_exists(u):
    print '<h1> Username, ' + u + ', already exists! </h1>'
else:
    if pwd == pwdc:
        insert_user(u, pwd, fn, ln, eml, bd, gen, game)
    else:
        print '<h1> Your passwords don\'t match </h1>'

print '''
</body>
</html>'''
