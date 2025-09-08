\c postgres;
drop database student;
create database student;

\c student;

create table students(
    id serial primary key,
    name VARCHAR(64),
    age int,
    student_group VARCHAR(64)
);

create table grades(
    id serial primary key,
    student_id int references students(id),
    subject VARCHAR(64),
    grade int
);

INSERT INTO students (name, age, student_group) VALUES
('Ali Valiyev', 20, 'CS-101'),
('Dilnoza Karimova', 22, 'CS-102'),
('Shohjahon Mardonov', 21, 'CS-101'),
('Malika Abdullayeva', 23, 'CS-103'),
('Jasur Akbarov', 20, 'CS-102');

INSERT INTO grades(student_id, subject, grade) VALUES
(1, 'Matematika', 90),
(1, 'Fizika', 85),
(2, 'Matematika', 95),
(2, 'Ingliz tili', 88),
(3, 'Dasturlash', 100),
(3, 'Matematika', 78),
(4, 'Fizika', 82),
(4, 'Dasturlash', 90),
(5, 'Dasturlash', 91),
(5, 'Ingliz tili', 84);

--3-masala
select name,student_group from students;

--4-masala
select students.name,students.age,students.student_group,
grades.subject,grades.grade from grades JOIN students on students.id = grades.student_id;

--5-masala
select name,age from students where age >20;

--6-masala
select students.name,avg(grades.grade) as overal_grade from students JOIN grades on students.id = grades.student_id group by students.name;

--7-masala
select student_group, count(*) as students from students group by student_group;

--8-masala
select students.name, grades.grade from students join grades on students.id = grades.student_id order by grades.grade desc limit 1;

--9-masala
select name from students where name like 'A%';

--10-masala
delete from students where student_group = 'Group C';
