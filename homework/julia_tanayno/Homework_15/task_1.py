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
cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ('Математика',))
subject_1 = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ('Геометрия',))
subject_2 = cursor.lastrowid

# Создали по два занятия для каждого предмета (lessons)
cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES(%s, %s)",
    ('Цифры', subject_1)
)
lesson_1 = cursor.lastrowid
cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES(%s, %s)",
    ('Числа', subject_1)
)
lesson_2 = cursor.lastrowid
cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES(%s, %s)",
    ('Катеты', subject_2)
)
lesson_3 = cursor.lastrowid
cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES(%s, %s)",
    ('Гипотенузы', subject_2)
)
lesson_4 = cursor.lastrowid

# Поставили своему студенту оценки (marks) для всех созданных вами занятий
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
    (5, lesson_1, student_id)
)
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
    (4, lesson_2, student_id)
)
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
    (4, lesson_3, student_id)
)
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
    (5, lesson_4, student_id)
)

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
