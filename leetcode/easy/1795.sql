-- https://leetcode.com/problems/rearrange-products-table/
-- 테이블의 출력 형식을 변환하는 문제

SELECT product_id, 'store1' AS store, store1 AS price FROM Products WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2' AS store, store2 AS price FROM Products WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3' AS store, store3 AS price FROM Products WHERE store3 IS NOT NULL

-- 해결 방법이 떠오르지 않아 답을 보고 해결
-- 둘 이상의 쿼리문의 결과를 'UNION'으로 합칠 수 있음(단, 컬럼의 개수와 테이터 타입이 같아야 함)
-- UNION은 중복 제거, UNION ALL은 중복 제거 X