/**
 * File: /DuplicateEmails.sql
 * Project: leetcode
 * Created Date: Saturday, August 5th 2017, 8:57:44 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Sat Aug 05 2017
 * Modified By: yanyan.yyy
 * -----
 */


# <https://leetcode.com/problems/duplicate-emails/description/>
Create table If Not Exists EmailPerson (Id int, Email varchar(255));
Truncate table EmailPerson;
insert into EmailPerson (`Id`, Email) values (1, 'a@b.com');
insert into EmailPerson (`Id`, Email) values (2, 'c@d.com');
insert into EmailPerson (`Id`, Email) values (3, 'a@b.com');

# old method
SELECT
    Email
FROM
(
    SELECT 
        Email, count(1) as cnt
    FROM EmailPerson
    GROUP BY Email
) a
WHERE 1=1
    and cnt>1;

# new
select 
    Email
from EmailPerson
group by Email
having count(distinct id) > 1;