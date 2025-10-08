-- Завдання 1
-- Створіть базу даних під назвою Sample. 
-- Розташування файлів залишається на ваш вибір.
-- #=======================================================================
-- Завдання 2
-- Переназвіть базу даних із першого завдання. 
-- Нове ім’я для бази даних Example.
-- #=======================================================================
-- Завдання 3
-- Видаліть базу даних Example.
-- #=======================================================================
-- Завдання 4
-- Створіть базу даних для зберігання оцінок студентів.
-- У базі даних створіть таблицю «Оцінки студентів», яка зберігатиме таку інформацію:
-- ■ ПІБ студента;
-- ■ місто;
-- ■ країна;
-- ■ дата народження;
-- ■ електронна адреса;
-- ■ контактний телефон;
-- ■ назва групи;
-- ■ середня оцінка за рік з усіх предметів;
-- ■ назва предмета з мінімальною, середньою оцінкою;
-- ■ назва предмета з максимальною, середньою оцінкою.
-- Наповніть цю базу даних трьома студентами.
-- #=======================================================================
-- Завдання 5
-- Створіть наступні запити для таблиці з оцінками
-- студентів із попереднього завдання:
-- ■ Відображати всієї інформації з таблиці зі студентами
-- та оцінками.
-- ■ Відображати ПІБ усіх студентів.
-- ■ Відображати усіх середніх оцінок.
-- ■ Показати ПІБ усіх студентів з мінімальною оцінкою,
-- більшою, ніж зазначена.
-- ■ Показати країни студентів. Назви країн мають бути
-- унікальними.
-- ■ Показати міста студентів. Назви міст мають бути
-- унікальними.
-- ■ Показати назви груп. Назви груп мають бути унікальними.
-- ■ Показати назви усіх предметів із мінімальними середніми оцінками. Назви предметів мають бути унікальними.

-- CREATE TABLE STUDENTS (
-- 	STUDENT_ID SERIAL PRIMARY KEY,
-- 	PIB VARCHAR(30),
-- 	CITY VARCHAR(30),
-- 	COUNTRY VARCHAR(30),
-- 	BIRTHDAY DATE,
-- 	EMAIL VARCHAR(40),
-- 	TELEPHONE VARCHAR(13),
-- 	GROUP_NAME VARCHAR(15),
-- 	AVG_GRATE DECIMAL,
-- 	MIN_SUBJECT_GRADE DECIMAL,
-- 	MIN_SUBJECT_NAME VARCHAR(20),
-- 	MAX_SUBJECT_GRADE DECIMAL,
-- 	MAX_SUBJECT_NAME VARCHAR(20)
-- )

-- INSERT INTO STUDENTS 
-- (PIB, CITY, COUNTRY, BIRTHDAY, EMAIL, TELEPHONE, GROUP_NAME, AVG_GRATE, MIN_SUBJECT_GRADE, MIN_SUBJECT_NAME, MAX_SUBJECT_GRADE, MAX_SUBJECT_NAME)
-- VALUES
-- ('Ivan Petrenko', 'Kyiv', 'Ukraine', '2003-04-15', 'ivan.petrenko@gmail.com', '+380931112233', 'IT-21', 88.5, 72.0, 'Math', 96.0, 'Programming'),
-- ('Olena Shevchenko', 'Lviv', 'Ukraine', '2002-09-10', 'olena.shevchenko@gmail.com', '+380631223344', 'DS-22', 91.2, 85.0, 'Statistics', 98.0, 'Machine Learning'),
-- ('Dmytro Kovalenko', 'Odesa', 'Ukraine', '2001-11-25', 'dmytro.kovalenko@gmail.com', '+380671112244', 'CS-20', 77.8, 60.0, 'Physics', 90.0, 'Algorithms'),
-- ('Anastasia Bondar', 'Kharkiv', 'Ukraine', '2003-02-08', 'anastasia.bondar@gmail.com', '+380992223344', 'IT-21', 83.6, 70.0, 'English', 95.0, 'Databases'),
-- ('Oleh Kravets', 'Dnipro', 'Ukraine', '2002-07-17', 'oleh.kravets@gmail.com', '+380991234567', 'CS-22', 85.0, 68.0, 'Math', 92.0, 'Programming'),
-- ('Yuliia Sydorenko', 'Poltava', 'Ukraine', '2003-12-29', 'yuliia.sydorenko@gmail.com', '+380971234555', 'DS-22', 89.4, 80.0, 'Statistics', 97.0, 'AI Systems'),
-- ('Andrii Melnyk', 'Vinnytsia', 'Ukraine', '2001-05-04', 'andrii.melnyk@gmail.com', '+380932345678', 'CS-20', 81.3, 65.0, 'Math', 94.0, 'Programming'),
-- ('Kateryna Horbunova', 'Ternopil', 'Ukraine', '2003-08-14', 'kateryna.horbunova@gmail.com', '+380953336677', 'IT-21', 90.1, 78.0, 'History', 99.0, 'Web Design'),
-- ('Serhii Lytvyn', 'Zhytomyr', 'Ukraine', '2002-03-22', 'serhii.lytvyn@gmail.com', '+380961234890', 'CS-22', 75.9, 60.0, 'Chemistry', 88.0, 'Networks'),
-- ('Iryna Zakharchenko', 'Chernihiv', 'Ukraine', '2001-10-05', 'iryna.zakharchenko@gmail.com', '+380931109988', 'DS-21', 87.2, 74.0, 'English', 93.0, 'Statistics'),
-- ('Maksym Tkachenko', 'Sumy', 'Ukraine', '2003-01-19', 'maksym.tkachenko@gmail.com', '+380981237654', 'IT-21', 84.5, 68.0, 'Biology', 90.0, 'Programming'),
-- ('Viktoria Romaniuk', 'Uzhhorod', 'Ukraine', '2002-11-12', 'viktoria.romaniuk@gmail.com', '+380991112200', 'DS-22', 91.0, 82.0, 'Math', 99.0, 'Data Analysis'),
-- ('Roman Shcherbak', 'Cherkasy', 'Ukraine', '2001-04-09', 'roman.shcherbak@gmail.com', '+380931555555', 'CS-20', 79.3, 62.0, 'English', 88.0, 'Programming'),
-- ('Nadiia Havryliuk', 'Ivano-Frankivsk', 'Ukraine', '2003-07-03', 'nadiia.havryliuk@gmail.com', '+380991112233', 'IT-21', 88.0, 76.0, 'Physics', 96.0, 'AI Systems'),
-- ('Taras Prokopenko', 'Lutsk', 'Ukraine', '2002-05-27', 'taras.prokopenko@gmail.com', '+380673330011', 'CS-22', 86.7, 70.0, 'Math', 95.0, 'Programming'),
-- ('Alina Boiko', 'Rivne', 'Ukraine', '2003-09-30', 'alina.boiko@gmail.com', '+380931223322', 'DS-22', 89.9, 81.0, 'English', 98.0, 'Machine Learning'),
-- ('Petro Oliinyk', 'Kyiv', 'Ukraine', '2002-06-16', 'petro.oliinyk@gmail.com', '+380931224466', 'CS-22', 84.7, 73.0, 'Physics', 92.0, 'Databases'),
-- ('Maria Danylko', 'Lviv', 'Ukraine', '2003-02-21', 'maria.danylko@gmail.com', '+380933335577', 'DS-22', 90.5, 85.0, 'Math', 97.0, 'Data Mining'),
-- ('Yaroslav Rudyk', 'Khmelnytskyi', 'Ukraine', '2001-09-13', 'yaroslav.rudyk@gmail.com', '+380961245678', 'IT-21', 83.2, 70.0, 'English', 91.0, 'Web Programming'),
-- ('Sofiia Chornyi', 'Mykolaiv', 'Ukraine', '2003-12-03', 'sofiia.chornyi@gmail.com', '+380993333222', 'DS-21', 88.8, 75.0, 'Chemistry', 94.0, 'Data Science');

SELECT * FROM STUDENTS;
SELECT PIB FROM STUDENTS;
SELECT PIB, AVG_GRATE FROM STUDENTS;
SELECT PIB FROM STUDENTS WHERE MIN_SUBJECT_GRADE > 80;
SELECT DISTINCT COUNTRY FROM STUDENTS;
SELECT DISTINCT CITY FROM STUDENTS;
SELECT DISTINCT GROUP_NAME FROM STUDENTS;
SELECT DISTINCT MIN_SUBJECT_NAME FROM STUDENTS WHERE MIN_SUBJECT_GRADE < 70;

-- STUDENTS WITH AVG GRADE GREATER THAN 60-80

SELECT * 
FROM STUDENTS
-- WHERE AVG_GRATE >= 60 AND AVG_GRATE <= 80
-- WHERE AVG_GRATE BETWEEN 60 AND 80
-- WHERE BIRTHDAY BETWEEN '2001-01-01' AND '2002-06-01'
-- WHERE CITY = 'Odesa' OR CITY = 'Poltava'
-- WHERE CITY IN ('Odesa', 'Poltava', 'Uzhhorod')
-- WHERE PIB LIKE '%nko'










