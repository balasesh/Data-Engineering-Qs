--  We want to run a new promotion for our most successful category of products (we call these categories “product classes”). Can you find out what are the top 3 selling product classes by total sales?

/* Ditinct sales records from the table */
select * from  
(
    select *,
    dense_rank() over (order by total_sales desc) as sales_rank
    from  vtrbusic.factsales
) Q1
where Q1.sales_rank <= 3
and Q1.category =  'product classes'

/*Non distnct  sales records*/
-- select * from  
-- (
--     select product_key,
--     SUM(total_sales),
--     dense_rank() over ( order by SUM(total_sales) desc) as total_sales_rank
--     from  vtrbusic.factsales
--         where category =  'product classes'
--     group by product_key
-- ) Q1
-- where Q1.total_sales_rank <= 3