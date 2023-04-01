# Write your MySQL query statement below
-- https://leetcode.com/problems/second-highest-salary/submissions/925872494/
# select MAX(salary) as SecondHighestSalary from Employee where salary <> (select MAX(salary) from Employee)

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary