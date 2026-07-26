-- RFM анализ клиентов

WITH customer_metrics AS (

    SELECT

        customer_id,

        MAX(order_date) AS last_order_date,

        COUNT(order_id) AS frequency,

        SUM(amount) AS monetary


    FROM orders


    WHERE status = 'completed'


    GROUP BY customer_id

)


SELECT

    customer_id,

    last_order_date,

    frequency,

    monetary,


    CASE

        WHEN frequency >= 10 THEN 'High'

        WHEN frequency >= 5 THEN 'Medium'

        ELSE 'Low'

    END AS frequency_segment,


    CASE

        WHEN monetary >= 500000 THEN 'VIP'

        WHEN monetary >= 200000 THEN 'Regular'

        ELSE 'Low Value'

    END AS value_segment


FROM customer_metrics


ORDER BY monetary DESC;
