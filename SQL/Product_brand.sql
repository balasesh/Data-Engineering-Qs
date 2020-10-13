/* 
 What brands have an average price above $3 and contain at least 2 different products?
 */

select brand_name, AVG(unit_price) , COUNT(brand_name)
from vtrbusic.product
GROUP BY brand_name
HAVING AVG(unit_price) > 300
AND COUNT(brand_name) >= 2

-- select brand_name
-- from db.product
-- GROUP BY brand_name
-- HAVING AVG(unit_price) > 3.00
-- AND COUNT(brand_name) >= 2