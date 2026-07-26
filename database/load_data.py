import pandas as pd
import psycopg2


conn = psycopg2.connect(
    database="sales_analytics",
    user="macbookair",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()


files = {
    "customers": "data/customers.csv",
    "products": "data/products.csv",
    "orders": "data/orders.csv",
    "order_items": "data/order_items.csv"
}


for table, file in files.items():

    df = pd.read_csv(file)

    print(
        f"Loading {table}: {len(df)} rows"
    )


    columns = list(df.columns)


    column_names = ",".join(columns)


    placeholders = ",".join(
        ["%s"] * len(columns)
    )


    query = f"""
        INSERT INTO {table}
        ({column_names})
        VALUES ({placeholders})
    """


    for row in df.itertuples(index=False):

        cursor.execute(
            query,
            tuple(row)
        )


    conn.commit()

    print(
        f"✅ {table} loaded"
    )


cursor.close()
conn.close()


print("🎉 All data loaded")
