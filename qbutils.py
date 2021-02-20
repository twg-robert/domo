import pypyodbc as pyodbc
import csv
import time

def qbtocsv(dsn, file_name, qb_query):
    cn = pyodbc.connect(dsn)
    cursor = cn.cursor()
    cursor.execute(qb_query)

    with open(file_name, 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow([x[0] for x in cursor.description])  
        wr.writerows(cursor.fetchall())
    cursor.close()
    cn.close()
