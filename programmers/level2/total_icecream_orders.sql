-- https://school.programmers.co.kr/learn/courses/30/lessons/133026

SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF F
JOIN ICECREAM_INFO I
ON F.FLAVOR = I.FLAVOR
GROUP BY INGREDIENT_TYPE