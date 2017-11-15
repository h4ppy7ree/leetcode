/**
 * File: /RankScores.sql
 * Project: DB
 * Created Date: Wednesday, November 15th 2017, 3:06:56 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Wed Nov 15 2017
 * Modified By: yanyan.yyy
 * -----
 */


-- https://leetcode.com/problems/rank-scores/description/
select
    a.score as Score
    , (select count(distinct score) from `Scores` where score>=a.score order by score desc) as Rank
from `Scores` a
order by score desc;