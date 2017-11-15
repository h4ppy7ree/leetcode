/**
 * File: /TripsUsers.sql
 * Project: DB
 * Created Date: Wednesday, November 15th 2017, 5:17:52 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Wed Nov 15 2017
 * Modified By: yanyan.yyy
 * -----
 */


-- https://leetcode.com/problems/trips-and-users/description/
/*
 1) find the cancellation rate of requests 
 2) made by unbanned clients 
 3) between Oct 1, 2013 and Oct 3, 2013
 4) the cancellation rate being rounded to two decimal places

 MySQL中ROUND和TRUNCATE的区别 
1、ROUND可以进行四舍五入，按照对应的位数 
2、TRUNCATE直接按照位数截取，不四舍五入
*/

select 
    Day
    , Round(sum_cancel_by_client/sum_all_req,2) as `Cancellation Rate`
from
(
    select
        sum(case when T.Status like "cancelled_by_%" then 1 else 0 end) as sum_cancel_by_client
        , sum(1) as sum_all_req 
        , T.Request_at as Day
    from 
        Trips T
    join Users U
    on 
        ( T.Client_Id=U.Users_Id 
            and U.Banned="No"
            and DATE_FORMAT(T.Request_at,"%m %d %Y")>="10 01 2013"
            and DATE_FORMAT(T.Request_at,"%m %d %Y")<="10 03 2013"
        )
    group by T.Request_at
) t
group by Day;



select
    T.Request_at as Day
    , Round(sum(case when T.Status like "cancelled_by_%" then 1 else 0 end)/sum(1) ,2) as `Cancellation Rate`  
from 
    Trips T
join Users U
on 
    ( T.Client_Id=U.Users_Id 
        and U.Banned="No"
        and DATE_FORMAT(T.Request_at,"%m %d %Y")>="10 01 2013"
        and DATE_FORMAT(T.Request_at,"%m %d %Y")<="10 03 2013"
    )
group by T.Request_at;