#import database.py
from database import userExists, deleteUser, insertUser, getMainPage

print('userExists("adducin")='+str(userExists('adducin')))
print('userExists("test2")='+str(userExists('test2')))
print('trying to delete user "test2"')
deleteUser('test2')
print('userExists("test2")='+str(userExists('test2')))
print('trying to insert user "test2"')
insertUser('test2', 'test2Pass', 'Test', '2', 'Test User 2 Desc', 'Hello World.pdf')
print('userExists("test2")='+str(userExists('test2')))
print('Database contents:')
getMainPage()
