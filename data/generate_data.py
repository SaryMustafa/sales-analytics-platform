import pandas as pd
import numpy as np
from faker import Faker
import random
import os


fake = Faker()

# количество записей
CUSTOMERS_COUNT = 10000
PRODUCTS_COUNT = 500
ORDERS_COUNT = 50000


os.makedirs("data", exist_ok=True)


# ==========================
# CUSTOMERS
# ==========================

customers = []

cities = [
    "Москва",
    "Санкт-Петербург",
    "Казань",
    "Новосибирск",
    "Екатеринбург",
    "Самара",
    "Ростов-на-Дону"
]


for i in range(1, CUSTOMERS_COUNT + 1):

    customers.append(
        {
            "customer_id": i,
            "name": fake.name(),
            "city": random.choice(cities),
            "registration_date": fake.date_between(
                start_date="-3y",
                end_date="today"
            )
        }
    )


customers_df = pd.DataFrame(customers)


# ==========================
# PRODUCTS
# ==========================

categories = [
    "Электроника",
    "Одежда",
    "Дом",
    "Спорт",
    "Красота",
    "Книги"
]


products = []


for i in range(1, PRODUCTS_COUNT + 1):

    products.append(
        {
            "product_id": i,
            "product_name": fake.word().capitalize(),
            "category": random.choice(categories),
            "price": random.randint(
                500,
                50000
            )
        }
    )


products_df = pd.DataFrame(products)



# ==========================
# ORDERS
# ==========================

orders = []


statuses = [
    "completed",
    "cancelled",
    "processing"
]


for i in range(1, ORDERS_COUNT + 1):

    customer_id = random.randint(
        1,
        CUSTOMERS_COUNT
    )


    orders.append(
        {
            "order_id": i,
            "customer_id": customer_id,
            "order_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            ),
            "status": random.choice(statuses),
            "amount": random.randint(
                1000,
                100000
            )
        }
    )


orders_df = pd.DataFrame(orders)



# ==========================
# ORDER ITEMS
# ==========================

order_items = []


for i in range(1, ORDERS_COUNT + 1):

    items_count = random.randint(
        1,
        5
    )


    for _ in range(items_count):

        product_id = random.randint(
            1,
            PRODUCTS_COUNT
        )


        order_items.append(
            {
                "order_id": i,
                "product_id": product_id,
                "quantity": random.randint(
                    1,
                    3
                )
            }
        )


order_items_df = pd.DataFrame(order_items)



# ==========================
# SAVE CSV
# ==========================

customers_df.to_csv(
    "data/customers.csv",
    index=False
)


products_df.to_csv(
    "data/products.csv",
    index=False
)


orders_df.to_csv(
    "data/orders.csv",
    index=False
)


order_items_df.to_csv(
    "data/order_items.csv",
    index=False
)



print("✅ Данные успешно созданы:")
print(
    f"Customers: {len(customers_df)}"
)
print(
    f"Products: {len(products_df)}"
)
print(
    f"Orders: {len(orders_df)}"
)
print(
    f"Order items: {len(order_items_df)}"
)
