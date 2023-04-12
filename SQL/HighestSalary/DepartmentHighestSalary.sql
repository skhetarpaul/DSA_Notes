-- https://leetcode.com/problems/department-highest-salary/description/
-- Following are the two approaches for the problem above using corelated subqueries and WHERE/IN clause.


# Write your MySQL query statement be
# select d1.name as Department, e1.name as Employee, salary as Salary from Employee e1 INNER JOIN department d1 ON d1.id = e1.departmentId where 0 = (select count(DISTINCT salary) from Employee e2 where e2.salary >e1.salary and e2.departmentId = e1.departmentId)

SELECT
  Department.name AS Department,
  Employee.name as Employee,
  Salary
FROM 
  Employee
INNER JOIN
  Department
ON
  Employee.departmentId = Department.id
WHERE (Employee.DepartmentId, salary) IN
(SELECT departmentId, max(salary) from Employee GROUP BY departmentId)