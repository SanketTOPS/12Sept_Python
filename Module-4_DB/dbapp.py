import sqlite3

dbcon=sqlite3.connect("newdb.db")

# Table Create
tbl_create="create table studinfo(id integer primary key autoincrement,name text,city text)"
try:
    dbcon.execute(tbl_create)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Records
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('mitesh','baroda'),('ashok','morbi'),('hitesh','surat'),('harsh','ahmedabad'),('pratik','rajkot')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update Records
"""update_data="update studinfo set city='gondal' where id=6"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Records
"""delete_data="delete from studinfo where id=6"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Show Data
cr=dbcon.cursor()

show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i)

except Exception as e:
    print(e)

