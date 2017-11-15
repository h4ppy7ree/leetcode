/**
 * File: /181.sql
 * Project: leetcode
 * Created Date: Saturday, August 5th 2017, 6:37:16 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Sat Aug 05 2017
 * Modified By: yanyan.yyy
 * -----
 */


# <https://leetcode.com/problems/employees-earning-more-than-their-managers/description/>

Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, ManagerId int);
Truncate table Employee;
insert into Employee (Id, Name, Salary, ManagerId) values ('1', 'Joe', '70000', '3');
insert into Employee (Id, Name, Salary, ManagerId) values ('2', 'Henry', '80000', '4');
insert into Employee (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', Null);
insert into Employee (Id, Name, Salary, ManagerId) values ('4', 'Max', '90000', Null);

SELECT
    a.Name as `Employee`
FROM `Employee` as a
join `Employee` as b
on a.ManagerId=b.Id
WHERE 1=1
    and a.Salary>b.Salary;