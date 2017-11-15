/**
 * File: /ConsecutiveNumbers.sql
 * Project: DB
 * Created Date: Wednesday, November 15th 2017, 3:23:21 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Wed Nov 15 2017
 * Modified By: yanyan.yyy
 * -----
 */


-- https://leetcode.com/problems/consecutive-numbers/description/
select
    DISTINCT a.Num as ConsecutiveNums
from Logs a
join Logs b on a.Id=b.Id-1
join Logs c on a.Id=c.Id-2
where a.Num=b.Num and b.Num=c.Num;