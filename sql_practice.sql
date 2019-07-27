select * from empdata
where salary > 198000 and hire_date > '2000-01-01';

select first_name, last_name, hire_date from empdata order by hire_date desc;

First person hired was Rosanne Mendoza
Last person hired was Phil Montgomery

select * from empdata where first_name = 'Jasmine'
UPDATE empdata
SET last_name = 'Johnson'
WHERE first_name = 'Jasmine'
select * from empdata where first_name = 'Jasmine'

select * from empdata where first_name = 'Doris'
DELETE FROM empdata where first_name = 'Doris'
select * from empdata where first_name = 'Doris'


To be safe one would use the emp_id instead of first_name for update and delete


