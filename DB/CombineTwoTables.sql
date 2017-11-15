/**
 * File: /CombineTwoTables.sql
 * Project: leetcode
 * Created Date: Saturday, August 5th 2017, 5:55:59 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Sat Aug 05 2017
 * Modified By: yanyan.yyy
 * -----
 */


# <https://leetcode.com/problems/combine-two-tables/description/>
SELECT
    a.FirstName
    , a.LastName
    , b.City
    , b.State
FROM 
    `Person` as a
    LEFT OUTER JOIN `Address` as b
    on a.PersonId=b.PersonId;