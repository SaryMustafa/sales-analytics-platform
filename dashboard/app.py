import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px


# =====================
# DATABASE CONNECTION
# =====================

conn = psycopg2.connect(
    database="sales_analytics",
    user="macbookair",
    host="localhost",
    port="5432"
)


st.set_page_config(
    page_title="Sales Analytics",
    layout="wide"
)


st.title(
    "📊 Sales Analytics Dashboard"
)


# =====================
# KPI
# =====================


query = """
SELECT
    SUM(amount) AS revenue,
    COUNT(order_id) AS orders,
    AVG(amount) AS avg_check
FROM orders
WHERE status='completed'
"""


kpi = pd.read_sql(
    query,
    conn
)


col1, col2, col3 = st.columns(3)


col1.metric(
    "💰 Revenue",
    f"{kpi.revenue[0]:,.0f}"
)


col2.metric(
    "📦 Orders",
    f"{kpi.orders[0]:,}"
)


col3.metric(
    "🧾 Average check",
    f"{kpi.avg_check[0]:,.0f}"
)



# =====================
# SALES BY MONTH
# =====================


st.subheader(
    "📈 Sales dynamics"
)


sales = pd.read_sql(
    """
    SELECT

        DATE_TRUNC(
            'month',
            order_date
        ) AS month,

        SUM(amount) AS revenue

    FROM orders

    WHERE status='completed'

    GROUP BY month

    ORDER BY month
    """,
    conn
)


fig = px.line(
    sales,
    x="month",
    y="revenue",
    markers=True,
    title="Revenue by month"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# =====================
# TOP CUSTOMERS
# =====================


st.subheader(
    "👥 Top customers"
)


customers = pd.read_sql(
    """

    SELECT

        c.name,

        SUM(o.amount) AS revenue


    FROM customers c


    JOIN orders o

    ON c.customer_id=o.customer_id


    WHERE o.status='completed'


    GROUP BY c.name


    ORDER BY revenue DESC


    LIMIT 10

    """,
    conn
)


fig = px.bar(
    customers,
    x="name",
    y="revenue",
    title="Top 10 customers"
)


st.plotly_chart(
    fig,
    use_container_width=True
)
# =====================
# TOP PRODUCTS
# =====================

st.subheader(
    "📦 Top products"
)


products = pd.read_sql(
    """

    SELECT

        p.product_name,

        p.category,

        SUM(oi.quantity) AS units_sold,

        SUM(
            oi.quantity * p.price
        ) AS revenue


    FROM order_items oi


    JOIN products p

    ON oi.product_id = p.product_id


    JOIN orders o

    ON oi.order_id = o.order_id


    WHERE o.status = 'completed'


    GROUP BY

        p.product_name,

        p.category


    ORDER BY revenue DESC


    LIMIT 10

    """,
    conn
)


fig = px.bar(
    products,
    x="product_name",
    y="revenue",
    color="category",
    title="Top 10 products by revenue"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.dataframe(
    products,
    use_container_width=True
)

# =====================
# RFM SEGMENTATION
# =====================

st.subheader(
    "👥 Customer Segmentation"
)


rfm = pd.read_sql(
    """

    WITH customer_metrics AS (

        SELECT

            customer_id,

            COUNT(order_id) AS frequency,

            SUM(amount) AS monetary


        FROM orders


        WHERE status='completed'


        GROUP BY customer_id

    )


    SELECT

        CASE

            WHEN frequency >= 10
            AND monetary >= 500000
            THEN 'VIP'


            WHEN frequency >= 5
            THEN 'Regular'


            ELSE 'Low Value'


        END AS segment,


        COUNT(*) AS customers


    FROM customer_metrics


    GROUP BY segment

    """,
    conn
)


fig = px.pie(
    rfm,
    names="segment",
    values="customers",
    title="Customer segments"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.dataframe(
    rfm,
    use_container_width=True
)

# =====================
# COHORT RETENTION
# =====================

st.subheader(
    "📈 Customer Retention Cohort"
)


cohort = pd.read_sql(
    """

    WITH first_purchase AS (

        SELECT

            customer_id,

            DATE_TRUNC(
                'month',
                MIN(order_date)
            ) AS cohort_month


        FROM orders


        WHERE status='completed'


        GROUP BY customer_id

    ),


    customer_activity AS (

        SELECT

            o.customer_id,

            fp.cohort_month,


            DATE_TRUNC(
                'month',
                o.order_date
            ) AS order_month


        FROM orders o


        JOIN first_purchase fp

        ON o.customer_id = fp.customer_id


        WHERE o.status='completed'

    )


    SELECT

        cohort_month,

        order_month,

        COUNT(
            DISTINCT customer_id
        ) AS customers


    FROM customer_activity


    GROUP BY

        cohort_month,

        order_month


    ORDER BY

        cohort_month,

        order_month

    """,
    conn
)


cohort["month_number"] = (
    (
        cohort["order_month"]
        -
        cohort["cohort_month"]
    )
    /
    pd.Timedelta(days=30)
).round()


retention = cohort.pivot_table(
    index="cohort_month",
    columns="month_number",
    values="customers"
)


retention = retention.divide(
    retention.iloc[:,0],
    axis=0
) * 100


fig = px.imshow(
    retention,
    labels=dict(
        x="Months after first purchase",
        y="Cohort",
        color="Retention %"
    ),
    title="Customer retention heatmap",
    text_auto=".1f"
)


st.plotly_chart(
    fig,
    use_container_width=True
)
