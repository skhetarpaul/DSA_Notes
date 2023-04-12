-- https://leetcode.com/problems/rank-scores/editorial/

# Write your MySQL query statement below
select score, DENSE_RANK() OVER (ORDER BY score DESC) as 'rank' from scores

-- check other methods from editorial as well.