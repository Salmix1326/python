-- Модуль 15. Вступ до теорії баз даних
-- Тема: Вступ до теорії баз даних.
-- Частина 2
-- Завдання 1
-- #==================================================================================================
-- Створіть наступні запити для бази даних з оцінками студентів із попереднього практичного завдання:
-- ■ Показати ПІБ усіх студентів з мінімальною оцінкою у вказаному діапазоні.
-- ■ Показати інформацію про студентів, яким виповнилося 20 років.
-- ■ Показати інформацію про студентів з віком, у вказаному діапазоні.
-- ■ Показати інформацію про студентів із конкретним ім’ям. Наприклад, показати студентів з ім’ям Борис.
-- ■ Показати інформацію про студентів, в номері яких є три сімки.
-- ■ Показати електронні адреси студентів, що починаються з конкретної літери.
-- #==================================================================================================
-- Завдання 2
-- Створіть наступні запити для бази даних з оцінками
-- студентів із попереднього практичного завдання:
-- ■ Показати мінімальну середню оцінку по всіх студентах.
-- ■ Показати максимальну середню оцінку по всіх студентах.
-- ■ Показати статистику міст. Має відображатися назва міста та кількість студентів з цього міста.
-- ■ Показати статистику студентів. Має відображатися назва країни та кількість студентів з цієї країни.
-- ■ Показати кількість студентів з мінімальною середньою оцінкою з математики.
-- ■ Показати кількість студентів з максимальною середньою оцінкою з математики.
-- ■ Показати кількість студентів у кожній групі.
-- ■ Показати середню оцінку групи.

SELECT PIB FROM STUDENTS WHERE MIN_SUBJECT_GRADE BETWEEN 70 AND 80;
SELECT * FROM STUDENTS WHERE (CURRENT_DATE - BIRTHDAY) >= 20;
SELECT * FROM STUDENTS WHERE AGE(BIRTHDAY) BETWEEN INTERVAL '22 YEARS' AND INTERVAL '23 YEARS';
SELECT * FROM STUDENTS WHERE PIB LIKE '%Alina%';
SELECT * FROM STUDENTS WHERE TELEPHONE LIKE '%5%5%';
SELECT * FROM STUDENTS WHERE EMAIL LIKE 'a%';
-- #==================================================================================================

SELECT * FROM STUDENTS;
SELECT MIN(AVG_GRATE) AS "MIN_AVG_GRADE" FROM STUDENTS;
SELECT MAX(AVG_GRATE) AS "MIN_AVG_GRADE" FROM STUDENTS;
SELECT CITY AS "CITY NAME", COUNT(*) AS "STUDENTS FROM CITY" FROM STUDENTS GROUP BY CITY;
SELECT COUNTRY AS "CITY NAME", COUNT(*) AS "STUDENTS FROM CITY" FROM STUDENTS GROUP BY COUNTRY;
SELECT COUNT(*) AS "MIN_AVG_GRADE MATH" FROM STUDENTS WHERE MIN_SUBJECT_NAME = 'Math';
SELECT COUNT(*) AS "MAX_AVG_GRADE ENGLISH" FROM STUDENTS WHERE MAX_SUBJECT_NAME = 'English';
SELECT GROUP_NAME AS "GROUP NAME", COUNT(*) AS "COUNT IN GROUP" FROM STUDENTS GROUP BY GROUP_NAME;
SELECT GROUP_NAME AS "GROUP NAME", AVG(AVG_GRATE) AS "AVG GRADE" FROM STUDENTS GROUP BY GROUP_NAME;
SELECT CITY, COUNT(CITY) FROM STUDENTS WHERE GROUP_NAME LIKE 'IT-21' GROUP BY CITY;

-- SUBVARIABLE
WITH MAXIMUM_AVG AS (SELECT MAX(AVG_GRATE) AS COLUMN_AVG FROM STUDENTS)

-- SELECT MAX(AVG_GRATE) FROM STUDENTS;
SELECT PIB, AVG_GRATE FROM STUDENTS, MAXIMUM_AVG WHERE AVG_GRATE = MAXIMUM_AVG.COLUMN_AVG;