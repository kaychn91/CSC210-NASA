#!C:\Python27\python.exe


import cgitb
import cgi
import datetime
import json
import hashlib
import MySQLdb as mdb
import sys

	
def SubmitArticle(username, text, title,platform,console):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	a = "INSERT into Articles(username, article_text, Title, Platform, Console) Values(%s, %s, %s, %s, %s)"
	cursor.execute(a, (username, text, title, platform, console))
	conn.commit()
	conn.close()

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

verify_user = cgi.FieldStorage()
fnc = verify_user['fnc'].value

result= {}

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

if fnc == 'submitarticle':
    username = verify_user['username'].value
    text = verify_user['atext'].value
    title = verify_user['atitle'].value
    platform = verify_user['platform'].value
    console = verify_user['console'].value
    SubmitArticle(username, text, title,platform,console)
    result['result'] = True
elif fnc == 'fetch':
    console = verify_user['console'].value
    result['result'] = fetchArticles(console)
else:
	pass

sys.stdout.write(json.dumps(result, indent=1))
sys.stdout.write("\n")

sys.stdout.close()
