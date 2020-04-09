# tgrio
Wrapper for accessing the website API

## Create a connection
``` python
import connection

conn = connection.Connection(username='secret_username',password='secret_password')
conn.connect()
```

## Import user information
``` python
import user

my_user = user.User(conn,'username_to_lookup')

#get user email
my_user.email

#print user attributes
print(my_user) 
```
