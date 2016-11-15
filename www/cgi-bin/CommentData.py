#!C:\Python27\python.exe


import cgitb
import cgi
import datetime
import json
import hashlib
import MySQLdb as mdb
import sys

	
def SubmitComment(username, articleID, CommentText):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	cmd = "INSERT into Comments(username, comment_text, articleid) Values(%s, %s, %s)"
	cursor.execute(cmd, (username, CommentText, articleID))
	
	conn.commit()
	conn.close()
	
def GetComments(articleID):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	c = conn.cursor()
	cmd = "SELECT username,commentid,comment_text FROM Comments where articleID=%s"
	c.execute(cmd, (articleID,))
	results = c.fetchall()
	conn.close()
	if len(results)>0:
		return results
	else:
		return False
	
cgitb.enable()

verify_user = cgi.FieldStorage()
fnc = verify_user['fnc'].value
articleID = verify_user['articleID'].value

result= {}

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

if fnc == 'submitcomment':
	username = verify_user['username'].value
	CommentText = verify_user['comment_text'].value
	SubmitComment(username, articleID, CommentText)
	result['result'] = True
elif fnc == 'GetComments':
	result['result'] = GetComments(articleID)
else:
	pass

sys.stdout.write(json.dumps(result, indent=1))
sys.stdout.write("\n")

sys.stdout.close()