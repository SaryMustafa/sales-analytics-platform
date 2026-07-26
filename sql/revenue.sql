-- Общая выручка

SELECT
    SUM(amount) AS total_revenue
FROM orders
WHERE status = 'completed';


-- Количество заказов

SELECT
    COUNT(*) AS total_orders
FROM orders
WHERE status = 'completed';


-- Средний чек

SELECT
    AVG(amount) AS average_order_value
FROM orders
WHERE status = 'completed';
