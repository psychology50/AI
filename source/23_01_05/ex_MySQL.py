# -- select sid, sname, deptno from student where deptno = 10;

# -- select distinct deptno, advisor from student -- distinct : 중복제거
# -- order by deptno;

# -- select sid, sname, deptno, grade from student where grade > 3.5 and gen = 'F';

# -- select pname, hiredate from professor where hiredate between '1990-01-01' and '1999-12-31';

# -- select sname, birthdate from student where addr = 'Daegu';
# -- select sname, birthdate from student where birthdate like '%-04-%'; -- % is same *

# -- select sname, length(sname), upper(sname) from student;

# -- select grade, round(grade / 4.5 * 100) grade100 from student;
# -- select birthdate, truncate(datediff(sysdate(), birthdate)/365, 0) age from student; -- 생일정보로 나이 구하기

# -- select deptno, avg(grade), sum(grade), max(grade), min(grade), count(*) from student group by deptno having count(*) <= 2; -- group by에서 where을 사용할 때 having
# -- select gen, avg(grade) from student group by gen;

# -- Sub Query
# -- select * from department where college = 'Engineering'; -- 공대생 학과번호 10, 20
# -- select * from student where deptno in (10, 20);
# -- 위의 과정을 하나로 묶기
# -- select * from student where deptno in (select deptno from department where college = 'Engineering');

# -- select * from student where grade > (select max(grade) from student where deptno = 10);
# -- select * from student where grade = (select max(grade) from student where gen = 'M') and gen = 'M';

# -- Join
# -- select sid, sname, dname from student s, department d where s.deptno = d.deptno order by sid;
# -- select sid, sname, dname from student s, department d where s.deptno = d.deptno and college = 'Engineering' order by sid;

# -- select sname, pname from student s, professor p where s.advisor = p.pid and p.hiredate >= '2000-01-01';

# -- select sid, sname, grade, pname, dname from student s, professor p, department d
# -- where s.advisor = p.pid and s.deptno = d.deptno and s.grade >= 3.0 order by dname, grade desc ;

# -- INSERT
# -- INSERT INTO department Values(10, 'Statistics', 'Sciences', 30000000);
# -- INSERT INTO student VALUES('1009', 'Jaeseo', '10', '101', 'M', 'Daegu', '1999-05-19', '4.5'); 

# -- UPDATE	
# -- UPDATE student SET deptno=10, addr='Daegu', grade=3.89 WHERE sname='Taehee';
# -- UPDATE student SET addr='Seoul' WHERE sname='Jaeseo';
# -- UPDATE student SET grade = grade+0.5 WHERE grade < 3.5;

# -- DELETE
# -- DELETE FROM student where sid >= 2000; 
# -- DELETE FROM department where deptno = 10;


# -- INSERT INTO mytable(mytable.desc, date)
# -- VALUES ('1st record', sysdate());

# -- INSERT INTO mytable(mytable.desc, date)
# -- VALUES ('2st record', sysdate());

# select * from mytable;

