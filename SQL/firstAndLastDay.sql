-- % Of sales that had a valid promotion, the VP of marketing wants to know what % of transactions occur on either the very first day or the very last day of a promotion campaign.

WITH trans_dates as (
    select 
        MIN(transaction_ts) as min_date, 
        MAX(transaction_ts) as max_date, 
        (select COUNT(product_type) from phumie1.completed_carts) rec_count
    from phumie1.completed_carts
    where promotion_id is not null
    )
SELECT
100 * (select count(product_type) from phumie1.completed_carts WHERE date(transaction_ts) = date(trans_dates.min_date)) / trans_dates.rec_count as min_percent,
100 * (select count(product_type) from phumie1.completed_carts WHERE date(transaction_ts) = date(trans_dates.max_date)) / trans_dates.rec_count as max_percent
from trans_dates
limit 1

----------------------------------------------

select 
(100 * sum(case when date(transaction_ts) = ( select date(min(transaction_ts)) from phumie1.completed_carts) then 1 else 0 END) / count(*))  as first_day_sales, 
(100 * sum(case when date(transaction_ts) = ( select date(max(transaction_ts)) from phumie1.completed_carts) then 1 else 0 END) / count(*))  as last_day_sales 
from phumie1.completed_carts