------------------ PROBLEM 1 ---------------------
/*
Q1. Write SQL query to find customers who have bought BOTH products 'iPhone 5s' AND also 'Samsung Note'. 
 */
-- 3 minutes

SELECT
    CUSTOMER_ID
FROM
    ORDERS
WHERE
    PRODUCT IN ('iPhone 5s', 'Samsung Note') -- check for both products assuming there are only these products
GROUP BY
    CUSTOMER_ID
HAVING
    COUNT(DISTINCT PRODUCT) = 2;

-- no of products
------------------ PROBLEM 2 ---------------------

/*
For all customers who have at least two orders, what is the average number of days elapsed between 1st and 2nd 
order (do not worry about using exact date functions)
 */
--15 Minutes

WITH temp AS
(
Select user_id, transaction_ts,
row_number() over (partition by user_id order by transaction_ts) as transaction_num
from phumie1.completed_carts 
) 
Select AVG(t2.transaction_ts - t1.transaction_ts) from 
temp t
LEFT JOIN temp t1 on t1.user_id = t.user_id and t1.transaction_num = 1
LEFT JOIN temp t2 on t2.user_id = t1.user_id and t2.transaction_num = 2
where 
t.transaction_num >= 2



/*
Which product had the highest sales with promotions and sales

- What are the top five (ranked in decreasing order) single-channel media types that correspond to the most money the grocery chain had spent on its promotional campaigns?  

% Of sales that had a valid promotion, the VP of marketing wants to know what % of transactions occur on either the very first day or the very last day of a promotion campaign.

Python:
Given an array containing None values fill in the None values with most recent non None value in the array
- input array: [1,None,2,3,None,None,5,None]
 - output array: [1,1,2,3,3,3,5,5]
*/

Select TOP 1 from (
	SELECT PRODUCT_ID, COUNT(PRODUCT_ID) AS SALES_COUNTS FROM PRODUCT_SALE
		where promotion = true
		GROUP BY PRODUCT_ID 
		ORDER BY SALES_COUNTS DESC
);

Select Channel_ids from media 
select * from grocery_chain_list where name = 'walmart' 
select TOP 5 Channels from table where 
channel_type = 'single'


