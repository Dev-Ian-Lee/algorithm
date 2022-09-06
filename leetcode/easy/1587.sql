-- https://leetcode.com/problems/bank-account-summary-ii/
-- 잔고 10000 이상의 사용자만 출력하는 문제

SELECT name, SUM(amount) AS balance
FROM Users JOIN Transactions ON Users.account = Transactions.account
GROUP BY Transactions.account
HAVING SUM(amount) > 10000

-- GROUP BY에 조건 줄 때는 WHERE 아닌 HAVING 사용
-- JOIN한 두 테이블에 같은 컬럼이 있을 경우, Transactions.account 같이 테이블명도 같이 명시