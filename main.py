# Модуль 18. Використання баз даних
# Тема: Використання баз даних. Частина 2
# ====================================================================================================
# Завдання
# Для бази даних Академія, яку ви розробили в рамках курсу «Теорія Баз Даних», створіть додаток для взаємодії з базою даних
# ■ передбачити можливість збереження звітів з результатів роботи на екран або у файл (встановлюється в налаштуваннях додатку);
# ■ передбачити можливість входу з різними рівнями доступу.
# Наприклад: доступ лише для читання, доступ для читання та запис, доступ для читання певних таблиць.
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker
import json


with open('credentials.json') as f:
    data = json.load(f)
    login = data['login']
    password = data['password']

DATABASE_URL = f"postgresql+psycopg2://{login}:{password}@localhost/ACADEMY"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
metadata.reflect(bind=engine)

tables = metadata.tables

# ====================================================================================================

# ■ вставляти рядки в таблиці бази даних
def insert_row_sql(table_name, row_data):
    if not row_data:
        print("No data provided to insert.")
        return

    columns = ', '.join(row_data.keys())
    placeholders = ', '.join([f":{col}" for col in row_data.keys()])
    sql = text(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})")

    try:
        session.execute(sql, row_data)
        session.commit()

        print(f"Row inserted into {table_name}.")

    except Exception as e:
        session.rollback()
        print(f"Error inserting row into {table_name}: {e}")


# ■ оновлювати рядків у таблицях бази даних
def update_row_sql(table_name, row_id, update_data):
    if not update_data:
        print("No data provided to update.")
        return

    set_clause = ', '.join([f"{col} = :{col}" for col in update_data.keys()])
    sql = text(f"UPDATE {table_name} SET {set_clause} WHERE id = :row_id")

    params = update_data.copy()
    params['row_id'] = row_id

    try:
        result = session.execute(sql, params)
        session.commit()

        if result.rowcount == 0:
            print(f"No row found with id {row_id} in {table_name}.")
        else:
            print(f"Row with id {row_id} updated in {table_name}.")

    except Exception as e:
        session.rollback()
        print(f"Error updating row in {table_name}: {e}")


# ■ видаляти рядки з таблиць бази даних
def delete_row_sql(table_name, row_id):
    sql = text(f"DELETE FROM {table_name} WHERE id = :row_id")

    try:
        result = session.execute(sql, {'row_id': row_id})
        session.commit()

        if result.rowcount == 0:
            print(f"No row found with id {row_id} in {table_name}.")
        else:
            print(f"Row with id {row_id} deleted from {table_name}.")

    except Exception as e:
        session.rollback()
        print(f"Error deleting row from {table_name}: {e}")


# ====================================================================================================
# ■ створювати звіти

# ▷ вивести інформацію про всі навчальні групи
def report_all_groups():
    sql = text("SELECT * FROM groups_table")

    try:
        result = session.execute(sql)
        groups = result.fetchall()

        for group in groups:
            print(group)

    except Exception as e:
        print(f"Error generating report for all groups: {e}")


# ▷ вивести інформацію про всіх викладачів
def report_all_teachers():
    sql = text("SELECT * FROM teachers")

    try:
        result = session.execute(sql)
        teachers = result.fetchall()

        for teacher in teachers:
            print(teacher)

    except Exception as e:
        print(f"Error generating report for all teachers: {e}")


# ▷ вивести назви усіх кафедр
def report_all_departments():
    sql = text("SELECT * FROM departments")

    try:
        result = session.execute(sql)
        departments = result.fetchall()

        for department in departments:
            print(department)

    except Exception as e:
        print(f"Error generating report for all departments: {e}")


# ▷ вивести імена та прізвища викладачів, які читають лекції в конкретній групі
def report_teachers_by_group(group_name):
    sql = text("""
        SELECT t.surname, t.name
        FROM groupslectures gl
        JOIN lectures l ON l.id = gl.lectureid
        JOIN groups_table gt ON gt.id = gl.groupid
        JOIN teachers t ON t.id = l.teacherid
        WHERE gt.name = :group_name
    """)

    try:
        result = session.execute(sql, {'group_name': group_name})
        teachers = result.fetchall()

        for teacher in teachers:
            print(teacher)

    except Exception as e:
        print(f"Error generating report for teachers by group {group_name}: {e}")


# ▷ вивести назви кафедр і груп, які до них відносяться
def report_departments_and_groups():
    sql = text("""
        SELECT d.name AS department_name, g.name AS group_name
        FROM departments d
        JOIN faculties f ON f.departmentid = d.id
        JOIN groups_table gt ON gt.departmentid = d.id
        ORDER BY d.name
    """)

    try:
        result = session.execute(sql)
        records = result.fetchall()

        for record in records:
            print(record)

    except Exception as e:
        print(f"Error generating report for departments and groups: {e}")


# ▷ відобразити кафедру з максимальною кількістю груп
def report_department_with_max_groups():
    sql = text("""
        SELECT d.name, COUNT(g.id) AS group_count
        FROM departments d
        JOIN faculties f ON f.departmentid = d.id
        JOIN groups_table gt ON gt.departmentid = d.id
        GROUP BY d.name
        ORDER BY group_count DESC
        LIMIT 1
    """)

    try:
        result = session.execute(sql)
        department = result.fetchone()

        if department:
            print(department)
        else:
            print("No departments found.")

    except Exception as e:
        print(f"Error generating report for department with max groups: {e}")


# ▷ відобразити кафедру з мінімальною кількістю груп
def report_department_with_min_groups():
    sql = text("""
        SELECT d.name, COUNT(gt.id) AS group_count
        FROM departments d
        JOIN faculties f ON f.departmentid = d.id
        JOIN groups_table gt ON gt.departmentid = d.id
        GROUP BY d.name
        ORDER BY group_count ASC
        LIMIT 1
    """)

    try:
        result = session.execute(sql)
        department = result.fetchone()

        if department:
            print(department)
        else:
            print("No departments found.")

    except Exception as e:
        print(f"Error generating report for department with min groups: {e}")


# ▷ вивести назви предметів, які викладає конкретний викладач
def report_subjects_by_teacher(teacher_surname):
    sql = text("""
        SELECT s.name AS subject_name
        FROM subjects s
        JOIN lectures l ON l.subjectid = s.id
        JOIN teachers t ON t.id = l.teacherid
        WHERE t.surname = :teacher_surname
    """)

    try:
        result = session.execute(sql, {'teacher_surname': teacher_surname})
        subjects = result.fetchall()

        for subject in subjects:
            print(subject)

    except Exception as e:
        print(f"Error generating report for subjects by teacher {teacher_surname}: {e}")


# ▷ вивести назви кафедр, на яких викладається конкретна дисципліна
def report_departments_by_subject(subject_name):
    sql = text("""
        SELECT DISTINCT d.name AS department_name
        FROM departments d
        JOIN faculties f ON f.departmentid = d.id
        JOIN groups_table gt ON gt.departmentid = d.id
        JOIN groupslectures gl ON gl.groupid = g.id
        JOIN lectures l ON l.id = gl.lectureid
        JOIN subjects s ON s.id = l.subjectid
        WHERE s.name = :subject_name
    """)

    try:
        result = session.execute(sql, {'subject_name': subject_name})
        departments = result.fetchall()

        for department in departments:
            print(department)

    except Exception as e:
        print(f"Error generating report for departments by subject {subject_name}: {e}")


# ▷ вивести назви груп, що належать до конкретного факультету
def report_groups_by_faculty(faculty_name):
    sql = text("""
        SELECT gt.name AS group_name
        FROM groups_table gt
        JOIN departments d ON d.id = gt.departmentid
        JOIN faculties f ON f.departmentid = d.id
        WHERE f.name = :faculty_name
    """)

    try:
        result = session.execute(sql, {'faculty_name': faculty_name})
        groups = result.fetchall()

        for group in groups:
            print(group)

    except Exception as e:
        print(f"Error generating report for groups by faculty {faculty_name}: {e}")


# ▷ вивести назви предметів та повні імена викладачів, які читають найбільшу кількість лекцій з них
def report_subjects_with_most_lectures():
    sql = text("""
        SELECT s.name AS subject_name, t.surname, t.name, COUNT(l.id) AS lecture_count
        FROM subjects s
        JOIN lectures l ON l.subjectid = s.id
        JOIN teachers t ON t.id = l.teacherid
        GROUP BY s.name, t.surname, t.name
        ORDER BY lecture_count DESC
        LIMIT 1
    """)

    try:
        result = session.execute(sql)
        record = result.fetchone()

        if record:
            print(record)
        else:
            print("No subjects found.")

    except Exception as e:
        print(f"Error generating report for subjects with most lectures: {e}")


# ▷ вивести назву предмету, за яким читається найменше лекцій
def report_subjects_with_least_lectures():
    sql = text("""
        SELECT s.name AS subject_name, COUNT(l.id) AS lecture_count
        FROM subjects s
        JOIN lectures l ON l.subjectid = s.id
        GROUP BY s.name
        ORDER BY lecture_count ASC
        LIMIT 1
    """)

    try:
        result = session.execute(sql)
        record = result.fetchone()

        if record:
            print(record)
        else:
            print("No subjects found.")

    except Exception as e:
        print(f"Error generating report for subjects with least lectures: {e}")


# ▷ вивести назву предмету, за яким читається найбільше лекцій
def report_subjects_with_most_lectures():
    sql = text("""
        SELECT s.name AS subject_name, COUNT(l.id) AS lecture_count
        FROM subjects s
        JOIN lectures l ON l.subjectid = s.id
        GROUP BY s.name
        ORDER BY lecture_count DESC
        LIMIT 1
    """)

    try:
        result = session.execute(sql)
        record = result.fetchone()

        if record:
            print(record)
        else:
            print("No subjects found.")

    except Exception as e:
        print(f"Error generating report for subjects with most lectures: {e}")


# Testing the functions
# =====================================================================================================
# insert_row_sql('departments', {'name': 'New Department', 'financing': 10000, 'facultyid': 5})
# update_row_sql('departments', 1, {'name': 'Updated Department', 'financing': 20000})
# delete_row_sql('departments', 6)

# report_all_groups()
# report_subjects_with_least_lectures()