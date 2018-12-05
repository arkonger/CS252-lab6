import mysql.connector
from mysql.connector import errorcode

#config = {
#	'user': 'root',
#	'password': '960Binnyy24',
#	'host': '',
#	'database': 'RESUME',
#	'raise_on_warnings': True
#}

#cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='RESUME', use_pure=False)
#cursor = cnx.cursor()

#query = "SELECT NAME, DESCRIPTION, RESUME_LOCALE FROM USERS WHERE USERNAME = %s"
#username = "'testUser'"

#print(query)

#query = query.replace('%s', username)

#print(query)

#cursor.execute(query)

#for(name, desc, locale) in cursor:
#	print("NAME={}\nDESCRIPTION={}\nRESUME_LOCALE={}".format(name, desc, locale))

#cursor.close()
#cnx.close()

def deleteUser(username):
	deleteQuery = "DELETE FROM RESUME.USERS WHERE USERS.USERNAME = '$username'"
	deleteQuery = deleteQuery.replace('$username', sanitizeIn(username),1)
	cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='RESUME', use_pure=False)
	cursor = cnx.cursor()
	cursor.execute(deleteQuery)
	cnx.commit()
	cursor.close()
	cnx.close()

def getMainPage():
	selectQuery = "SELECT us.USERNAME, us.FIRSTNAME, us.LASTNAME, us.DESCRIPTION, us.RESUME_LOCALE FROM RESUME.USERS us"
	cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='RESUME', use_pure=False)
	cursor = cnx.cursor()
	cursor.execute(selectQuery)
	htmlDocContents = ''
	for username, firstname, lastname, description, resume_locale in cursor:
		htmlDocContents += htmlWrap(username, firstname, lastname, description, resume_locale)
	cursor.close()
	cnx.close()
	return htmlDocContents;

def htmlWrap(username, firstname, lastname, description, resume_locale):
	html = "<"
	print(username+'\t|\t'+firstname+'\t|\t'+lastname+'\t|\t'+description+'\t|\t'+resume_locale)
	html += ">"
	return html

def userExists(username):
	userNameQuery = "SELECT USERS.USERNAME FROM RESUME.USERS WHERE USERS.USERNAME = '"+sanitizeIn(username)+"';"
	cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='RESUME', use_pure=False)
	cursor = cnx.cursor()
	cursor.execute(userNameQuery)
	for name, in cursor:
		if name == sanitizeIn(username):
			cursor.close()
			cnx.close()
			return True
	cursor.close()
	cnx.close()
	return False

def userPassExists(username, password):
	userNameQuery = "SELECT USERS.USERNAME, USERS.PASSWORD FROM RESUME.USERS WHERE USERS.USERNAME='"+sanitizeIn(username)+"' AND USERS.PASSWORD='"+sanitizeIn(password)+"';"
	cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='RESUME', use_pure=False)
	cursor = cnx.cursor()
	cursor.execute(userNameQuery)
	for name, passW in cursor:
		if name == sanitizeIn(username) and passW == sanitizeIn(passW):
			cursor.close()
			cnx.close()
			return True
	cursor.close()
	cnx.close()
	return False

	


def insertUser6(username, password, firstname, lastname, description, resume_locale):
	insertQuery = "INSERT INTO USERS(USERNAME, PASSWORD, FIRSTNAME, LASTNAME, DESCRIPTION, RESUME_LOCALE) VALUES('$username', '$password', '$firstname', '$lastname', '$description', '$resume_locale');"
	insertQuery = insertQuery.replace('$username', sanitizeIn(username), 1)
	insertQuery = insertQuery.replace('$password', sanitizeIn(password), 1)
	insertQuery = insertQuery.replace('$firstname', sanitizeIn(firstname), 1)
	insertQuery = insertQuery.replace('$lastname', sanitizeIn(lastname), 1)
	insertQuery = insertQuery.replace('$description', sanitizeIn(description), 1)
	insertQuery = insertQuery.replace('$resume_locale', sanitizeIn(resume_locale), 1)
	cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='RESUME', use_pure=False)
	cursor = cnx.cursor()
	#print(insertQuery)
	cursor.execute(insertQuery)
	cnx.commit()
	cursor.close()
	cnx.close()
	#print('exit "insertUser()"')


def insertUser4(username, password, firstname, lastname):
	insertQuery = "INSERT INTO USERS(USERNAME, PASSWORD, FIRSTNAME, LASTNAME) VALUES('$username', '$password', '$firstname', '$lastname');"
	insertQuery = insertQuery.replace('$username', sanitizeIn(username), 1)
	insertQuery = insertQuery.replace('$password', sanitizeIn(password), 1)
	insertQuery = insertQuery.replace('$firstname', sanitizeIn(firstname), 1)
	insertQuery = insertQuery.replace('$lastname', sanitizeIn(lastname), 1)
	cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='RESUME', use_pure=False)
	cursor = cnx.cursor()
	cursor.execute(insertQuery)
	cnx.commit()
	cursor.close()
	cnx.close()

def sanitizeIn(val):
	sanVal = val
	if(sanVal is None):
		sanVal = ''
	sanVal = sanVal.replace(';', '', sanVal.count(';'))
	sanVal = sanVal.replace('\'', '\\\'', sanVal.count('\''))
	sanVal = sanVal.replace('"', '\\"', sanVal.count('"'))
	return sanVal
