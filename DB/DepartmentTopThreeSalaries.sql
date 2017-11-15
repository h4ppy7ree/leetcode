/**
 * File: /DepartmentTopThreeSalaries.sql
 * Project: DB
 * Created Date: Wednesday, November 15th 2017, 4:28:05 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Wed Nov 15 2017
 * Modified By: yanyan.yyy
 * -----
 */


--  https://leetcode.com/problems/department-top-three-salaries/description/
select
    D.Name as Department
    , E1.Name as Employee
    , E1.Salary as Salary
from Employee E1
join Department D on D.Id=E1.DepartmentId
where
( select
    count(distinct Salary) as cnt
from Employee E2 
where E1.DepartmentId=E2.DepartmentId
    and E1.Salary<=E2.Salary
) <= 3
order by DepartmentId, Salary desc;