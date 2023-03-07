-- https://school.programmers.co.kr/learn/courses/30/lessons/157342

SELECT CAR_ID, ROUND(AVG(DURATION), 1) AS AVERAGE_DURATION
FROM (SELECT CAR_ID, DATEDIFF(END_DATE, START_DATE) + 1 AS DURATION 
     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) T

GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC