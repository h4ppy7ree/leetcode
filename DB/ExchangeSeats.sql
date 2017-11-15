/**
 * File: /ExchangeSeats.sql
 * Project: DB
 * Created Date: Wednesday, November 15th 2017, 2:39:09 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Wed Nov 15 2017
 * Modified By: yanyan.yyy
 * -----
 */


-- https://leetcode.com/problems/exchange-seats/description/
SELECT 
    a.id as id
    , case
        when mod(a.id, 2) = 0 then (select student from `seat` where id=a.id-1)
        when mod(a.id, 2) != 0 and a.id < (select count(1) from `seat`) then ( select student from `seat` where id=a.id+1)
        else student
    end as student
FROM `seat` as a;