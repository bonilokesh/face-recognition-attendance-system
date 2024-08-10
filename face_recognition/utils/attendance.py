from dotenv import dotenv_values
import mysql.connector
from openpyxl import Workbook
import datetime

wb = Workbook()
ws = wb.active

secrets = dotenv_values("C:/Users/bonil/Desktop/face_recognition/.env")

add_attendence_query = "INSERT INTO attendance(course_name, solt, user_email, attended, added_date) VALUES(%s, %s, %s, %s, %s)"
get_attendence_query = "SELECT * FROM attendance WHERE user_email = %s"

config = {
    "host": secrets['DB_HOST_URL'],
    "port": secrets['DB_PORT'],
    "database": secrets['DB_DATABASE'],
    "user": secrets['DB_USERNAME'],
    "password": secrets['DB_PASSWORD'],
    "charset": "utf8",
    "use_unicode": True,
    "get_warnings": True,
}

def mark_attendence(course_name, slot, user_email, attended):
    print("insert.....")
    
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor()   
    
    rows = list()
    for email in user_email:
        d = datetime.datetime.now().strftime("%I:%M%p %B %d, %Y")
        ws.append([course_name, slot, email, attended, d])
        rows.append(
            (course_name, slot, email, attended, d)
        )
    
    wb.save("C:/Users/bonil/Desktop/face_recognition/static/sample.xlsx")
    cur.executemany(add_attendence_query, rows)
    cnx.commit()

    cur.close()
    cnx.close()
   
def get_attendance(email):
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor()
    
    cur.execute(get_attendence_query, (email, ))
    res = cur.fetchall()
    
    cur.close()
    cnx.close()
    
    return res


