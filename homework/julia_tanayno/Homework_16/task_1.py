import csv
import mysql.connector as mysql
import os
from dotenv import load_dotenv

# в какой папке находится текущий файл
base_path = os.path.dirname(__file__)
# поднялись на два уровня выше (до homework)
homework_path = os.path.dirname(os.path.dirname(base_path))
csv_path = os.path.join(
    homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv'
)

load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)

cursor = db.cursor(dictionary=True)

cursor.execute('''SELECT s.name, s.second_name, g.title as group_title,
b.title as book_title, sub.title as subject_title,
l.title as lesson_title, m.value as mark_value
FROM students s
LEFT JOIN `groups` g
ON s.group_id = g.id
LEFT JOIN books b
ON s.id = b.taken_by_student_id
LEFT JOIN marks m
ON s.id = m.student_id
LEFT JOIN lessons l
ON m.lesson_id = l.id
LEFT JOIN subjects sub
ON l.subject_id = sub.id''')

data_result = cursor.fetchall()

with open(csv_path, newline="") as csv_file:
    file_data = csv.DictReader(csv_file)
    for row in file_data:
        if row not in data_result:
            print(row)

db.close()
