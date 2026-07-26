SELECT
    DATE_TRUNC(
        'month',
        order_date
    ) AS month,

    COUNT(order_id) AS orders,

    SUM(amount) AS revenue

FROM orders

WHERE status = 'completed'

GROUP BY month

ORDER BY month;
