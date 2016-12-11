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
	currentdate = str(datetime.datetime.now())
	a = "INSERT into Articles(username, article_text, Title, Platform, Console, TimeCreated) Values(%s, %s, %s, %s, %s, %s)"
	cursor.execute(a, (username, text, title, platform, console, currentdate))
	conn.commit()
	b = "Select ArticleID from Articles where username= %s && TimeCreated = %s"
	cursor.execute(b, (username, currentdate))
	result = cursor.fetchall()
	if(len(result)==1):
		for row in result:
			aid = row[0]
	conn.close()
	return aid

def Save_Uploaded_File(form_field, articleid):
	conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
	cursor = conn.cursor()
	currentdate = str(datetime.datetime.now())
	a = "INSERT into Images(ArticleID, Time_Created) Values(%s,%s)"
	cursor.execute(a, (articleid,currentdate))
	conn.commit()
	b = "Select ImageId from Images where articleID=%s && Time_Created =%s"
	cursor.execute(b, (articleid, currentdate))
	result = cursor.fetchall()
	fnm = ""
	if(len(result)==1):
		for row in result:
			fnm = str(row[0])
	conn.close()
	if not verify_user.has_key(form_field): 
		raise ValueError(form_field + 'field in form not found')
	fileitem = verify_user[form_field]
	if not fileitem.file: 
		raise ValueError('file doesnt have any appended files')
	fout = file(os.path.join("F:\Web-Dev-Class\www\Article-Images", fnm+".png"), 'wb')
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
	cmd = "SELECT ArticleID,Title,left(article_text,100) FROM Articles WHERE Console=%s LIMIT 10"
	c.execute(cmd, (console,))
	results = c.fetchall()
	conn.close()
	if len(results)>0:
		return results
	else:
		return False

def getImages(articleid):
	conn = mdb.connect(db='csc210', host='localhost', user='root', passwd='mysql')
	c=conn.cursor()
	cmd = "select ImageId from Images where ArticleID = %s"
	c.execute(cmd, (articleid,))
	results = c.fetchall()
	conn.close()
	if len(results)>0:
		return results
	else:
		return False
	
def getRecent():
    conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
    c = conn.cursor()
    cmd = "SELECT ArticleID,Title,left(article_text,100) FROM Articles ORDER BY TimeCreated DESC LIMIT 13"
    c.execute(cmd)
    results = c.fetchall()
    conn.close()
    if len(results)>0:
        return results
    else:
        return False

def userAs(username):
    conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
    c = conn.cursor()
    cmd = "SELECT ArticleID,Title FROM Articles WHERE username=%s LIMIT 10"
    c.execute(cmd, (username,))
    results = c.fetchall()
    conn.close()
    if len(results)>0:
        return results
    else:
        return False

def delete(aid):
    conn = mdb.connect(db='csc210',host='localhost',user='root',passwd='mysql')
    c = conn.cursor()
    b = "SELECT ImageId FROM Images WHERE ArticleID=%s"
    c.execute(b, (aid,))
    results = c.fetchall()
    e = "DELETE FROM Images WHERE ArticleID=%s"
    c.execute(e, (aid,))
    a = "DELETE FROM Comments WHERE articleid=%s"
    c.execute(a, (aid,))
    d = "DELETE FROM Articles WHERE ArticleID=%s"
    c.execute(d, (aid,))
    conn.commit()
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
	articleid = SubmitArticle(username, text, title, platform, console)
	result['result'] = True
	result['articleid'] = articleid
elif fnc == 'fetch':
	console = verify_user['console'].value
	result['result'] = fetchArticles(console)
elif fnc == 'getarticle':
	articleID = verify_user['articleID'].value
	result['result'] = GetArticle(articleID)
	result['images'] = getImages(articleID)
elif fnc == 'upload_image':
	imageno = verify_user['imageno'].value
	articleid = verify_user['articleid'].value
	for i in range(int(imageno)):
		Save_Uploaded_File("file" + str(i), articleid)
	result['result'] = True
elif fnc == 'getAs':
    user = verify_user['username'].value
    result['result'] = userAs(user)
elif fnc =='recent':
    result['result']=getRecent()
elif fnc == 'del':
	aid = verify_user['aid'].value
	ims = delete(aid)
	for index in ims:
		#fnm=ims[index]
		os.remove("F:/Web-Dev-Class/www/Article-Images/"+str(index[0])+".png")
	result['result'] = True

sys.stdout.write(json.dumps(result, indent=1))
sys.stdout.write("\n")

sys.stdout.close()
