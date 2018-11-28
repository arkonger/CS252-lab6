import mysql.connector
from mysql.connector import errorcode

config = {
	'user': 'root',
	'password': '960Binnyy24',
	'host': '',
	'database': 'RESUME',
	'raise_on_warnings': True
}

cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='RESUME', use_pure=False)
cursor = cnx.cursor()

query = "SELECT NAME, DESCRIPTION, RESUME_LOCALE FROM USERS WHERE USERNAME = %s"
username = "'testUser'"

print(query)

query = query.replace('%s', username)

print(query)

cursor.execute(query)

for(name, desc, locale) in cursor:
	print("NAME={}\nDESCRIPTION={}\nRESUME_LOCALE={}".format(name, desc, locale))

cursor.close()
cnx.close()


