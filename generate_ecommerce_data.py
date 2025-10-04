import csv
import random
from datetime import date, timedelta

"""
This script generates a synthetic e‑commerce sales dataset. The resulting
CSV file will be written to the ``../data`` directory relative to this script.

This version avoids using external dependencies like ``faker`` and instead
relies on Python's built‑in ``datetime`` module to produce random dates.
"""

def main() -> None:
    """Entry point for generating the dataset."""
    # Seed the random number generator for reproducible results
    random.seed(42)

    # Define the number of rows and possible values for each column
    n_rows = 800
    genders = ['Male', 'Female', 'Other']
    regions = ['North', 'South', 'East', 'West']
    categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports']
    payments = ['Credit Card', 'Paypal', 'Debit Card']

    # Predefined price ranges for each product category
    price_range = {
        'Electronics': (80, 500),
        'Clothing': (20, 120),
        'Home & Kitchen': (50, 250),
        'Books': (10, 40),
        'Sports': (60, 200)
    }

    data = []
    # Define the range of dates for orders
    start_date = date(2023, 1, 1)
    end_date = date(2023, 3, 31)
    delta_days = (end_date - start_date).days
    for i in range(n_rows):
        order_id = 10001 + i
        # Generate a random date between start_date and end_date
        order_date = start_date + timedelta(days=random.randint(0, delta_days))
        cust_id = f"CUST{str(i+1).zfill(3)}"
        gender = random.choices(genders, weights=[0.48, 0.48, 0.04])[0]
        age = random.randint(18, 65)
        region = random.choice(regions)
        category = random.choice(categories)
        amount = round(random.uniform(*price_range[category]), 2)
        payment = random.choices(payments, weights=[0.6, 0.3, 0.1])[0]
        data.append([
            order_id,
            order_date,
            cust_id,
            gender,
            age,
            region,
            category,
            amount,
            payment
        ])

    # Define column headers for the CSV
    headers = [
        "OrderID",
        "OrderDate",
        "CustomerID",
        "Gender",
        "Age",
        "Region",
        "ProductCategory",
        "OrderAmount",
        "PaymentMethod",
    ]
    # Determine the output path relative to the location of this script.  This
    # ensures the script can be executed from any working directory.
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '..', 'data', 'ecommerce_sales_data.csv')
    # Create the parent directory if it doesn't already exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        # Convert date objects to ISO format strings when writing
        for row in data:
            # row[1] is a date; convert to ISO string
            row_to_write = row.copy()
            row_to_write[1] = row_to_write[1].isoformat()
            writer.writerow(row_to_write)
    print(f"Dataset saved to {output_path}")

if __name__ == '__main__':
    main()