/**
 * File: /SecondHighestSalary.sql
 * Project: leetcode
 * Created Date: Saturday, August 5th 2017, 10:18:13 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Sat Aug 05 2017
 * Modified By: yanyan.yyy
 * -----
 */


# <https://leetcode.com/problems/second-highest-salary/description/>
;


SELECT 
    Salary as SecondHighestSalary
FROM Employee
UNION SELECT null
order by SecondHighestSalary desc
limit 1, 1;