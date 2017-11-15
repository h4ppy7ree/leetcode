/**
 * File: /DepartmentHighestSalary.sql
 * Project: DB
 * Created Date: Wednesday, November 15th 2017, 3:48:44 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Wed Nov 15 2017
 * Modified By: yanyan.yyy
 * -----
 */


-- https://leetcode.com/problems/department-highest-salary/description/
select
    D.Name as Department
    , E.Name as Employee
    , E.Salary as Salary
from
    Employee E
    , Department D
    , ( 
        select
            max(Salary) as Salary
            , DepartmentId
        from Employee
        group by DepartmentId ) M
WHERE 
    E.Salary=M.Salary
    and E.DepartmentId=M.DepartmentId
    and D.Id=M.DepartmentId
;