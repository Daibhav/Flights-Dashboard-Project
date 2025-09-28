import mysql.connector
import os

username = os.environ.get('username')
pwd = os.environ.get('password')

# connect to the database server
try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = username,
        password = pwd,
        database = 'indigo'

    )
    mycursor = conn.cursor()
    print('connection established')
except:
    print('connection error')    

# create a database on the db server
#mycursor.execute("CREATE DATABASE indigo")    
#conn.commit()

# create a table : airport -> airport_id | code | name | city

# mycursor.execute("""
# create table airport(
#     airport_id integer primary key,
#     code varchar(10) not null,
#     city varchar(50) not null,
#     name varchar(255) not null
# )
# """)
# conn.commit()

# insert data to the table
# mycursor.execute("""
                 
#     insert into airport values
#     (1, 'DEL','New Delhi','IGIA'),
#     (2, 'CCU','Kolkata','NSCA'),
#     (3, 'BOM','Mumbai','CSMA')                 
# """)
# conn.commit()

# search/retieve
mycursor.execute('select * from airport where airport_id>1')
data =  mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

# update
mycursor.execute("""
update airport
set name = 'Bombay'
where airport_id = 3                 
""")  
conn.commit()  

# delete
mycursor.execute('delete from airport where airport_id = 3')
conn.commit()
mycursor.execute('select * from airport')
data2 = mycursor.fetchall()
print(data2)
