#!C:\Python27\python.exe


import cgitb
import cgi
import datetime
import json
import hashlib
import MySQLdb as mdb
import sys

	
def SubmitArticle(username, text, title):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	a = "INSERT into Articles(username, article_text, Title, Platform, Console) Values(%s, %s, %s, %s, %s)"
	cursor.execute(a, (username, text, title, platform, console))
	conn.commit()
	conn.close()


cgitb.enable()

verify_user = cgi.FieldStorage()
fnc = verify_user['fnc'].value
platform = verify_user['platform'].value
console = verify_user['console'].value
result= {}

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

if fnc == 'submitarticle':
    username = verify_user['username'].value
    text = verify_user['atext'].value
    title = verify_user['atitle'].value
    SubmitArticle(username, text, title)
    result['result'] = True
else:
	pass

sys.stdout.write(json.dumps(result, indent=1))
sys.stdout.write("\n")

sys.stdout.close()