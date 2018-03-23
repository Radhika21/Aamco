SELECT SUM(amount) from payment;

SELECT SUM(amount) from payment
WHERE DATEOFPAYMENT BETWEEN DATE '2018-01-01' AND DATE '2018-01-28';

SELECT * from student
WHERE (FirstName LIKE 'D%') AND (LastName LIKE 'G%');

SELECT student.student_ID, SUM(payment.amount)
FROM payment INNER JOIN student
ON payment.STUDENT_ID = student.STUDENT_ID
WHERE (student.STUDENT_ID BETWEEN 2018125 AND 2018175) AND (payment.student_ID = student.student_ID) group by student.student_ID ORDER BY student.student_ID;

SELECT instructor.FirstName, instructor.LastName, student.student_ID, student.FirstName, student.LastName
FROM instructor INNER JOIN student
ON student.instructor_ID = instructor.INSTRUCTOR_ID
WHERE (student.student_ID BETWEEN 2018340 AND 2018400) AND (student.instructor_ID = instructor.instructor_ID) AND instructor.instructor_ID = 4;

SELECT instructor.FirstName, COUNT(student.student_ID)
FROM instructor INNER JOIN student
ON instructor.instructor_ID = student.instructor_ID
GROUP BY instructor.FirstName ORDER BY instructor.FirstName;

SELECT COUNT(*) FROM student;