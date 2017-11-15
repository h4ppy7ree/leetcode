/**
 * File: /RisingTemperature.sql
 * Project: leetcode
 * Created Date: Saturday, August 5th 2017, 9:15:23 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Sat Aug 05 2017
 * Modified By: yanyan.yyy
 * -----
 */


# <https://leetcode.com/problems/rising-temperature/description/>
SELECT 
    W2.Id
FROM `Weather` as W1, `Weather` as W2 
WHERE 1=1
    and TO_DAYS(W1.Date)=TO_DAYS(W2.Date)-1
    and W2.Temperature>W1.Temperature;

SELECT 
    W2.Id
FROM `Weather` as W1, `Weather` as W2 
WHERE 1=1
    and DATEDIFF(W2.Date, W1.Date)=1
    and W2.Temperature>W1.Temperature;

UPDATE Weather
SET Temperature='20'
WHERE `Date`='2015-01-01';

SELECT Temperature, count(1) from Weather
GROUP BY Temperature;