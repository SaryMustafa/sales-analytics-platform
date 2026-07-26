-- Cohort Analysis

WITH first_purchase AS (

    SELECT

        customer_id,

        MIN(order_date) AS first_order_date


    FROM orders


    WHERE status = 'completed'


    GROUP BY customer_id

),


customer_orders AS (

    SELECT

        o.customer_id,

        o.order_date,

        fp.first_order_date,


        DATE_TRUNC(
            'month',
            fp.first_order_date
        ) AS cohort_month,


        DATE_TRUNC(
            'month',
            o.order_date
        ) AS order_month


    FROM orders o


    JOIN first_purchase fp

    ON o.customer_id = fp.customer_id


    WHERE o.status = 'completed'

)


SELECT

    cohort_month,

    order_month,

    COUNT(
        DISTINCT customer_id
    ) AS active_customers


FROM customer_orders


GROUP BY

    cohort_month,

    order_month


ORDER BY

    cohort_month,
    order_month;
