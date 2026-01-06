

-- Preview first rows
select *
from sales_data
limit 5;


-- Check null values
SELECT COUNT(*)
FROM sales_data
WHERE sales IS NULL OR profit IS NULL;


-- Check duplicate orders
SELECT order_id, COUNT(*)
FROM sales_data
GROUP BY order_id
HAVING COUNT(*) > 1;


-- Check negative sales
SELECT *
FROM sales_data
WHERE sales < 0;






-- Calculate total sales
select sum(sales) as total_sales
from sales_data;


-- Calculate total profit
select sum(profit) as total_profit
from sales_data;

-- Total orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales_data;




-- Sales per category
select category,
       sum(sales) as total_sales
	   from sales_data
	   group by category
	   order by total_sales DESC;



--Top 10 products by sales
select "sub-category",
       sum(sales) as total_sales
	   from sales_data
	   group by "sub-category"
	   order by total_sales DESC
	   limit 10;


-- Profit by category
SELECT
    category,
    SUM(profit) AS total_profit
FROM sales_data
GROUP BY category
ORDER BY total_profit DESC;



-- Orders with negative profit
SELECT
    order_id,
    "sub-category",
    sales,
    profit
FROM sales_data
WHERE profit < 0
ORDER BY profit;


-- Shipping before order (data issue)
SELECT *
FROM sales_data
WHERE ship_date < order_date;



-- Monthly sales trend
select 
     DATE_TRUNC('month', order_date) as Month,
	 sum(sales) as total_sales
	 from sales_data
	 group by month
	 order by month;


-- MoM growth calculation
SELECT
    month,
    total_sales,
    total_sales - LAG(total_sales) OVER (ORDER BY month) AS mom_growth
FROM (
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        SUM(sales) AS total_sales
    FROM sales_data
    GROUP BY month
);
	 
	   



