from mysql.connector import connection

fakedb = connection.MySQLConnection(
     user='user',
     password='user',
     host='127.0.0.1',
     database='testdb'
)   

cursor = fakedb.cursor()

cursor.execute("DROP TABLE IF EXISTS thunder_info")

sql = '''CREATE TABLE thunder_info(
CODI_EMP INT,
SOLICITANTE VARCHAR(255),
TIPO VARCHAR(255),
COMP_DAS CHAR(7),
VALOR_DAS CHAR(10), 
PATH_DAS CHAR(255),
ALIQ_ISS CHAR(10)
)'''

cursor.execute(sql)

sql = """INSERT INTO thunder_info VALUES (
'0001','ROMULO','FORFUN', '01/2024', '2000.00', NULL, NULL
)"""
cursor.execute(sql)

sql = """INSERT INTO thunder_info VALUES (
'0002','ALISSON', 'CPM22', '02/2024', '2000.00', NULL, NULL
)"""
cursor.execute(sql)

sql = """INSERT INTO thunder_info VALUES (
'0003','ANDERSON','ANDERFATHER RESTAURANT','03/2024','2000.00', NULL, NULL
)"""
cursor.execute(sql)


sql = """INSERT INTO thunder_info VALUES (
'0004','EDUARDO','COSTA CONTABILIDADE','04/2024','2000.00', NULL, NULL
)"""
cursor.execute(sql)

try: 
    fakedb.commit()  # Committing after all commands

except Exception as e:
    print(e)
    fakedb.rollback()  # Rolling back in case of error 

fakedb.close()
