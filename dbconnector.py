import mysql.connector as conn
con=conn.connect(host='localhost',user='root',password='root',database='annaiclg')
cursor=con.cursor()
cursor.execute('select * from staff')
rows=cursor.fetchall()
for i in rows:
    print('staff id:',i[0])
    print('staff name:',i[1])

