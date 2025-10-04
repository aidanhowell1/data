import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
random.seed(42)
Faker.seed(42)

n_rows = 800
genders = ['Male', 'Female', 'Other']
regions = ['North', 'South', 'East', 'West']
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports']
payments = ['Credit Card', 'Paypal', 'Debit Card']

data = []
for i in range(n_rows):
    order_id = 10001 + i
    order_date = fake.date_between(start_date='2023-01-01', end_date='2023-03-31')
    cust_id = f"CUST{str(i+1).zfill(3)}"
    gender = random.choices(genders, weights=[0.48, 0.48, 0.04])[0]
    age = random.randint(18, 65)
    region = random.choice(regions)
    category = random.choice(categories)
    price_range = {
        'Electronics': (80, 500),
        'Clothing': (20, 120),
        'Home & Kitchen': (50, 250),
        'Books': (10, 40),
        'Sports': (60, 200)
    }
    amount = round(random.uniform(*price_range[category]), 2)
    payment = random.choices(payments, weights=[0.6, 0.3, 0.1])[0]
    data.append([order_id, order_date, cust_id, gender, age, region, category, amount, payment])

df = pd.DataFrame(data, columns=[
    "OrderID", "OrderDate", "CustomerID", "Gender", "Age", "Region",
    "ProductCategory", "OrderAmount", "PaymentMethod"
])

df.to_csv('ecommerce_sales_data.csv', index=False)