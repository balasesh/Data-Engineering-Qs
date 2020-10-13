-- We are considering running a promo across brands. We want to target customers who have bought products from two specific brands. Can you find out which customers have bought products from both the “Fort West" and the "Golden" brands?

-- customer -> product -> brand_name

SELECT
    customer_id 
FROM
    vtrbusic.factsales FS
    INNER JOIN (
        SELECT
            product_key
        FROM
            vtrbusic.product
        WHERE
            brand_name in ('Fort West')
    ) FP1 ON FP1.product_key = FS.product_key
    INNER JOIN (
        SELECT
            product_key
        FROM
            vtrbusic.product
        WHERE
            brand_name in ('Golden')
    ) FP2 ON FP2.product_key = FS.product_key

-- SELECT customer_id
-- FROM vtrbusic.factsales FS
-- WHERE 1 = 1
--   AND EXISTS
--     (
--      SELECT 1
--      FROM vtrbusic.product FP
--      WHERE FP.product_key = FS.product_key
--      AND FP.brand_name in ('Fort West') 
--     )
--   AND EXISTS
--     (
--      SELECT 1
--      FROM vtrbusic.product FP
--      WHERE FP.product_key = FS.product_key 
--      AND FP.brand_name in ('Golden')
--     )

SELECT
    CUSTOMER_ID
FROM
    ORDERS
WHERE
    PRODUCT IN ('Fort West', 'Golden') -- check for both products assuming there are only these products
GROUP BY
    CUSTOMER_ID
HAVING
    COUNT(DISTINCT PRODUCT) = 2;