/**
 * File: /ClassesMoreThan5Students.sql
 * Project: leetcode
 * Created Date: Saturday, August 5th 2017, 9:31:19 pm
 * Author: yanyan.yyy
 * -----
 * Last Modified: Sat Aug 05 2017
 * Modified By: yanyan.yyy
 * -----
 */


# <https://leetcode.com/problems/classes-more-than-5-students/description/>
/* There is a table courses with columns: student and class

Please list out all classes which have more than or equal to 5 students.

For example, the table:

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
Should output:

+---------+
| class   |
+---------+
| Math    |
+---------+
Note:
The students should not be counted duplicate in each course. */
SELECT
    class
FROM courses
GROUP BY class
Having count(distinct student)>=5;
# 注意观察测试数据，里面是有重复的数据