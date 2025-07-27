
-- Below query calculates number of days of consecutive price increase (postgres sql)
-- Business Analyst Interview: write a SQL query to find out the employee ID who came to the office for most consecutive days
-- https://medium.com/@mail2asimmanna/a-beautiful-sql-question-from-my-business-analyst-interview-8d46e1adbb3c

-- Create table
CREATE TABLE t (
    product VARCHAR(10),
    dt DATE,
    price DECIMAL(10,2)
);

-- Insert data for product 'A' (note gaps in the dates)
INSERT INTO t (product, dt, price) VALUES
('A', '2024-07-01', 10.00),
('A', '2024-07-03', 12.00),
('A', '2024-07-04', 15.00),
('A', '2024-07-06', 14.00),
('A', '2024-07-07', 16.00);

-- Insert data for product 'B'
INSERT INTO t (product, dt, price) VALUES
('B', '2024-07-01', 9.00),
('B', '2024-07-02', 8.00),
('B', '2024-07-04', 12.00),
('B', '2024-07-05', 13.00),
('B', '2024-07-08', 14.00);


WITH price_with_lag AS (
  SELECT
    product,
    dt,
    price,
    LAG(price) OVER (PARTITION BY product ORDER BY dt) AS prev_price FROM t
),
increase_flags AS (
  SELECT
    *,
    CASE 
      WHEN price > prev_price THEN 1
      ELSE 0
    END AS is_increase FROM price_with_lag
),
x AS (
  SELECT *,
  ROW_NUMBER() OVER (PARTITION BY increase_flags.product ORDER BY increase_flags.dt) AS rnk
  FROM increase_flags WHERE is_increase = 1
),
y AS (
  SELECT x.product,
         x.dt,
	     x.rnk,
         date(x.dt - x.rnk::double precision * '1 days'::interval) AS day_1,
         x.price FROM x
	)
,z AS (
   SELECT y.product,
   y.day_1,
   MIN(y.dt) AS beg_dt,
   MAX(y.dt) AS end_dt,
   COUNT(y.day_1) AS cnt_consecutive_d FROM y
   GROUP BY y.product, y.day_1)
SELECT * FROM z