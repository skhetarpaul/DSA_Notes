# Write your MySQL query statement b

SELECT d.name as Department, e1.Name as Employee, e1.salary as Salary from employee e1 
INNER JOIN department d ON e1.departmentId = d.id
where 
3 > (select COUNT(DISTINCT salary) from employee e2 where e2.salary > e1.salary AND e1.departmentId = e2.departmentId)