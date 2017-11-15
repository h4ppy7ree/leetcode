/**
 * File: /183.sql
 * Project: leetcode
 * Created Date: Saturday, August 5th 2017, 9:07:30 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Sat Aug 05 2017
 * Modified By: yanyan.yyy
 * -----
 */


# <https://leetcode.com/problems/customers-who-never-order/description/>
SELECT 
    C.Name as Customers
FROM `Customers` as C 
left outer join Orders as O
on C.Id=O.CustomerId
WHERE 1=1
    and O.CustomerId is NULL;

SELECT A.Name from Customers A
WHERE A.Id NOT IN (SELECT B.CustomerId from Orders B)