from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker
import json

with open('credentials.json') as f:
    data = json.load(f)
    login = data['login']
    password = data['password']

DATABASE_URL = f"postgresql+psycopg2://{login}:{password}@localhost/HOSPITAL"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
metadata.reflect(bind=engine)

tables = metadata.tables

# ================================================================================================================

# Завдання 1
# Для бази даних «Лікарня», яку ви розробляли в рамках курсу «Теорія Баз Даних», створіть додаток для взаємодії з
# базою даних, який дозволяє:
# ■ Вставляти рядки в таблиці бази даних.
# ■ Оновлення рядків у таблицях бази даних.
# При спробі оновлення усіх рядків в одній таблиці надайте запит на підтвердження користувачеві.
# Оновлювати усі рядки можна лише після підтвердження користувачем.
# ■ Видалення рядків з таблиць баз даних.
# При спробі видалити усі рядки в одній таблиці потрібно видавати користувачу запит на підтвердження.
# Видаляти усі рядки, можна тільки після підтвердження користувачем.
# ================================================================================================================

# Завдання 2
# Для бази даних «Лікарня», яку ви розробляли в рамках курсу «Теорія Баз Даних»,
# створіть додаток для взаємодії з базою даних, який дозволяє створювати звіти:
# ▷ Вивести прізвища лікарів та їх спеціалізації;
# ▷ Вивести прізвища та зарплати (сума ставки та надбавки) лікарів, які не перебувають у відпустці;
# ▷ Вивести назви палат, які знаходяться у певному відділенні;
# ▷ Вивести усі пожертвування за вказаний місяць у вигляді: відділення, спонсор, сума пожертвування, дата пожертвування;
# ▷ Вивести назви відділень без повторень, які спонсоруються певною компанією.
# ================================================================================================================

# Завдання 3
# Для бази даних «Лікарня», яку ви створювали в рамках курсу «Теорія баз даних», реалізуйте програму,
# яка дозволить працювати зі структурою бази даних.
# Програма має:
# ■ відображати назви усіх таблиць;
# ■ відображати назви стовпців певної таблиці;
# ■ відображати назви стовпців та їх типи для певної таблиці;
# ■ відображати зв’язки між таблицями;
# ■ вміти створювати таблиці;
# ■ видаляти таблиці;
# ■ додавати стовпці;
# ■ оновлювати стовпці;
# ■ видаляти стовпці.
# ================================================================================================================

def show_tables_names():
    print("Tables in the database:")

    for table_name in tables.keys():
        print(f"- {table_name}")


def show_doctors_specializations():
    query_text = """
    SELECT DOCTORS.SURNAME, SPECIALIZATIONS.NAME
    FROM DOCTORS
    join DOCTORSSPECIALIZATIONS on DOCTORS.id = DOCTORSSPECIALIZATIONS.doctor_id
    join SPECIALIZATIONS on DOCTORSSPECIALIZATIONS.specialization_id = SPECIALIZATIONS.id
    """

    query = session.execute(text(query_text))
    print("Doctors and their specializations:")

    for row in query:
        print(f"- Doctor's surname: {row.surname}. Specializations: {row.name}")


def show_doctors_salaries_not_on_leave():
    query_text = """
    SELECT DISTINCT DOCTORS.SURNAME, (DOCTORS.SALARY + DOCTORS.PREMIUM) AS TOTAL_SALARY
    FROM DOCTORS
    join VACATIONS on DOCTORS.id = VACATIONS.doctor_id
    WHERE VACATIONS.ENDDATE < CURRENT_DATE OR VACATIONS.STARTDATE > CURRENT_DATE
    """

    query = session.execute(text(query_text))
    print("Doctors not on leave and their salaries:")

    for row in query:
        print(f"- Doctor's surname: {row.surname}. Total Salary: {row.total_salary}")


# show_tables_names()
# show_doctors_specializations()
# show_doctors_salaries_not_on_leave()