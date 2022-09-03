-- https://leetcode.com/problems/find-total-time-spent-by-each-employee/
-- 각 직원이 매일 사무실에 있었던 시간을 출력하는 문제
-- SUM, COUNT와 같은 집계함수는 서브쿼리를 사용할 필요없이, 원하는 조건(날짜, 직원)을 GROUP BY에 명시

SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id

-- Easy 난이도였는데도 헷갈리고 시간이 오래 걸렸음 
-- -> SQL 연습도 꾸준히