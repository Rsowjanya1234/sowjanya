import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='sowjanya',
                     db='demo1',
                     cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
query = 'INSERT INTO student VALUES("JOHN", "DOLLY", 24, "00028")'
try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()
