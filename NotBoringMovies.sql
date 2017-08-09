/**
 * File: /NotBoringMovies.sql
 * Project: leetcode
 * Created Date: Saturday, August 5th 2017, 5:39:20 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Sat Aug 05 2017
 * Modified By: yanyan.yyy
 * -----
 */


# <https://leetcode.com/problems/not-boring-movies/description/>
SELECT 
    *
FROM `cinema`
WHERE 1=1
    and id%2=1
    and description<>'boring'
order by rating desc;