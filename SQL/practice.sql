-- Q1. Write SQL query to find customers who have bought BOTH products 'iPhone 5s' AND also 'Samsung Note'. 


Select customer_id from orders 
where product in ('iPhone 5s', 'Samsung Note'. )
Group by customer_id
having distinct count(DISTINCT PRODUCT) = 2


-- For all customers who have at least two orders, what is the average number of days elapsed between 1st and 2nd order (do not worry about using exact date functions)

Select customer_id, 
desnse_rank () over (order by transaction_dt asc)
from orders 
Group by customer_id
having distinct count(order_id) >= 2