/**
 * File: /HumanTrafficStadium.sql
 * Project: DB
 * Created Date: Wednesday, November 15th 2017, 5:54:41 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Wed Nov 15 2017
 * Modified By: yanyan.yyy
 * -----
 */


-- https://leetcode.com/problems/human-traffic-of-stadium/description/
/*
1) 3 or more consecutive rows 
2) the amount of people more than 100(inclusive)
*/
--增加一列用于计数
select
    id
    , date
    , people
    , case when people>=100 then @cnt:=@cnt+1 else @cnt:=0 end as cnt
from stadium
    ,(select @cnt:=0) var
order by id asc;


select
    a.id
    , a.date
    , a.people
from stadium a
, (                 #得到计数为3和比3更大的id值
    select       
        cnt
        , id
    from
    (               #增加一列用于计数
        select
            id
            , date
            , people
            , case when people>=100 then @cnt:=@cnt+1 else @cnt:=0 end as cnt
        from stadium
            ,(select @cnt:=0) var
        order by id asc
    ) t
    where t.cnt>=3
) b
where (b.cnt=3 and (a.id=b.id or a.id=b.id-1 or a.id=b.id-2))   #计数等于3时，需要打印前两行以及本行
or (b.cnt>3 and (a.id=b.id))   #计数大于3时，需要打印 
order by id asc;