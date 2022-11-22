import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='sowjanya',
                     database='demo1',
                     cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print('database version: %s ' % data)
