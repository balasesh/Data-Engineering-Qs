-- To improve sales, the marketing department runs various types of promotions. The marketing manager would like to analyze the effectiveness of these promotion campaigns. In particular, what percent of our sales transactions had a valid promotion applied?

SELECT 100.00 * 
COUNT(product_item_id) / ( select COUNT(product_item_id) from phumie1.completed_carts) 
AS promotion_sales_percent
from phumie1.completed_carts
where promotion_id is NOT NULL