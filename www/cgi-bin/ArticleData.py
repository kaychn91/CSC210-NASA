#!C:\Python27\python.exe


import cgitb
import cgi
import datetime
import json
import hashlib
import MySQLdb as mdb
import sys, os
try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

verify_user = cgi.FieldStorage()

def SubmitArticle(username, text, title, platform, console):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	a = "INSERT into Articles(username, article_text, Title, Platform, Console) Values(%s, %s, %s, %s, %s)"
	cursor.execute(a, (username, text, title, platform, console))
	conn.commit()
	conn.close()

def Save_Uploaded_File(form_field):
	if not verify_user.has_key(form_field): 
		raise ValueError(form_field + 'field in form not found')
	fileitem = verify_user[form_field]
	if not fileitem.file: 
		raise ValueError('file doesnt have any appended files')
	fout = file(os.path.join("F:\Web-Dev-Class\www\images", fileitem.filename), 'wb')
	while 1:
		chunk = fileitem.file.read(100000)
		if not chunk: break
		fout.write(chunk)
	fout.close()

def GetArticle(articleID):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	c = conn.cursor()
	cmd = "SELECT username,Title,article_text,Platform,Console FROM Articles WHERE ArticleID=%s"
	c.execute(cmd, (articleID,))
	results = c.fetchall()
	conn.close()
	if len(results)>0:
		return results
	else:
		return False

def fetchArticles(console):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	c = conn.cursor()
	cmd = "SELECT ArticleID,Title FROM Articles WHERE Console=%s"
	c.execute(cmd, (console,))
	results = c.fetchall()
	conn.close()
	if len(results)>0:
		return results
	else:
		return False

cgitb.enable()

fnc = verify_user['fnc'].value
result= {}

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

if fnc == 'submitarticle':
	platform = verify_user['platform'].value
	console = verify_user['console'].value
	username = verify_user['username'].value
	text = verify_user['atext'].value
	title = verify_user['atitle'].value
	SubmitArticle(username, text, title, platform, console)
	result['result'] = True
elif fnc == 'fetch':
	console = verify_user['console'].value
	result['result'] = fetchArticles(console)
else:
	imageno = verify_user['imageno'].value
	for i in range(int(imageno)):
		Save_Uploaded_File("file" + str(i))
	result['result'] = True

sys.stdout.write(json.dumps(result, indent=1))
sys.stdout.write("\n")

sys.stdout.close()