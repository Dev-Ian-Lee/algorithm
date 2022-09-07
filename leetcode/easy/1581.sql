-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.visit_id IS NULL
GROUP BY customer_id

-- 문제 조건(PK) 잘 확인하기
-- WHERE, GROUP BY 같이 사용 가능
-- HAVING절에는 GROUP BY, 집계함수에서 사용한 컬럼만 사용 가능