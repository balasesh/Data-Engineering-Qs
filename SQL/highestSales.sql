--Which product had the highest sales with promotions and sales ( basically a where clause on 2 flags)

Select product_id, MAX(total_sales) from sales
where 
sales_type = 'promotions' or 
sales_type = 'sales'
GROUP BY product_id
limit 1