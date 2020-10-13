--Find top 5 sales products having promotions
Select product_id from "tablename"
where promotion_id is not null
order by units_sold desc
limit 5

select * from (
Select product_id,SUM(units_sold),
dense_rank() over (order by SUM(units_sold) desc) as product_rank
from "tablename" 
where promotion_id is not null
GROUP BY product_id
) where product_rank <= 5