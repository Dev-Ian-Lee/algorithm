-- https://leetcode.com/problems/capital-gainloss/
-- 각 물품의 손익을 출력하는 문제

SELECT stock_name, SUM(
    CASE
        WHEN operation='Buy' THEN -price
        ELSE price
    END
) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name

-- SELECT stock_name, SUM(
--     IF(operation='Buy', -1, 1) * price
-- ) AS capital_gain_loss
-- FROM Stocks
-- GROUP BY stock_name

-- 계속 시도해봤지만, 해결할 수 없어 답을 보고 해결
-- CASE문, IF문을 SQL에서도 사용 가능

-- operation이 'Buy'일 때는 값을 빼고, 'Sell'일 때는 값을 더함