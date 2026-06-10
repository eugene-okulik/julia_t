import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)
# Создали студента (student)
cursor.execute(
    "INSERT INTO students (name, second_name) VALUES ('Remco', 'Vasserman')"
)
student_id = cursor.lastrowid
cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
print(cursor.fetchone())

# Создали несколько книг (books) и указали, что их взял созданный студент
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    query, [
        ('My Python', student_id),
        ('My Java', student_id),
        ('My Ruby', student_id)
    ]
)

# Создали группу (group) и определили своего студента туда
cursor.execute(
    '''
    INSERT INTO `groups` (title, start_date, end_date)
    VALUES ('group 215', 'oct 2026', 'dec 2026')
    '''
)
groups_id = cursor.lastrowid
cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s", (
        groups_id, student_id
    )
)

# Создали несколько учебных предметов (subjects)
subjects = {}
for title in ['Математика', 'Геометрия']:
    cursor.execute(
        "INSERT INTO subjects (title) VALUES (%s)",
        (title,)
    )
    subjects[title] = cursor.lastrowid

# Создали по два занятия для каждого предмета (lessons)
lessons_data = [
    ('Цифры', subjects['Математика']),
    ('Числа', subjects['Математика']),
    ('Катеты', subjects['Геометрия']),
    ('Гипотенузы', subjects['Геометрия'])
]
lessons = {}

for title, subject_id in lessons_data:
    cursor.execute(
        "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
        (title, subject_id)
    )
    lessons[title] = cursor.lastrowid

# Поставили своему студенту оценки (marks) для всех созданных вами занятий
values = [
    (5, lessons['Цифры'], student_id),
    (4, lessons['Числа'], student_id),
    (4, lessons['Катеты'], student_id),
    (5, lessons['Гипотенузы'], student_id),
]
query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(query, values)

db.commit()
# Получили информацию из базы данных:
# Все оценки студента
cursor.execute(
    "SELECT * from marks WHERE student_id = (%s)",
    (student_id,)
)
print(cursor.fetchall())

# Все книги, которые находятся у студента
cursor.execute(
    "SELECT * from books WHERE taken_by_student_id = (%s)",
    (student_id,)
)
print(cursor.fetchall())

# Для вашего студента выведите всё, что о нем есть в базе:
# группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)

cursor.execute('''SELECT s.name, s.second_name, g.title as group_title,
b.title as book_title, sub.title as subject_title,
l.title as lesson_title, m.value as mark
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
ON l.subject_id = sub.id
WHERE s.id = (%s)''', (student_id,))
print(cursor.fetchall())

db.close()
