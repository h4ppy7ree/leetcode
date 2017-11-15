/**
 * File: /DeleteDuplicateEmails.sql
 * Project: leetcode
 * Created Date: Saturday, August 5th 2017, 9:46:35 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Sat Aug 05 2017
 * Modified By: yanyan.yyy
 * -----
 */


# <https://leetcode.com/problems/delete-duplicate-emails/description/>
SELECT 
    MIN(Id) as Id
    , Email
FROM Person 
GROUP BY Email;

DELETE FROM EmailPerson 
WHERE Id NOT IN (
    select t.id from (
        SELECT 
            MIN(Id)
        FROM EmailPerson 
        GROUP BY Email
    ) t
);