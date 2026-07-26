-- Количество клиентов

SELECT
    COUNT(DISTINCT customer_id) AS customers_count
FROM orders
WHERE status = 'completed';



-- Топ клиентов по выручке

SELECT

    c.customer_id,

    c.name,

    c.city,

    COUNT(o.order_id) AS orders_count,

    SUM(o.amount) AS total_revenue


FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id


WHERE o.status = 'completed'


GROUP BY
    c.customer_id,
    c.name,
    c.city


ORDER BY total_revenue DESC


LIMIT 10;
