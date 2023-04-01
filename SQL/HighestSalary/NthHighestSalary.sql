-- Note that how we have created a special SQL function
--Also note, LIMIT query is the fastest
-- Corelated subquery is slower as compared to the LIMIT query.


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET  n = N-1;
  RETURN (
      # Write your MySQL query statement below.
      # SELECT distinct e1.salary from Employee e1 WHERE N-1 = (SELECT count(DISTINCT e2.salary) from Employee e2 where e2.salary> e1.salary)

      SELECT DISTINCT salary from Employee GROUP BY salary ORDER BY salary DESC LIMIT n,1
  );
ENDCREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET  n = N-1;
  RETURN (
      # Write your MySQL query statement below.
      # SELECT distinct e1.salary from Employee e1 WHERE N-1 = (SELECT count(DISTINCT e2.salary) from Employee e2 where e2.salary> e1.salary)

      SELECT DISTINCT salary from Employee GROUP BY salary ORDER BY salary DESC LIMIT n,1
  );
END