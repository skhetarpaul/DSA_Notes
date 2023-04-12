# Write your MySQL query statement below
# select e1.id, e1.salary as salary, e2.salary as managerSalary, e1.name from employee e1 left join employee e2 on e1.managerId  = e2.id;
select temp.name as Employee  from (select e1.id, e1.salary as salary, e2.salary as managerSalary, e1.name from employee e1 inner join employee e2 on e1.managerId  = e2.id) as temp where salary>managerSalary