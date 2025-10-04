# E-commerce Synthetic Sales Dataset

This repository contains a realistic synthetic dataset for showcasing data analysis skills, as well as a Python script to generate the data.

## Files

- **ecommerce_sales_data.csv**: Main synthetic dataset (~800 rows, 9 columns)
- **generate_ecommerce_data.py**: Script to regenerate the dataset

## Data Dictionary

| Column           | Type        | Description                                                     |
|------------------|-------------|-----------------------------------------------------------------|
| OrderID          | Numeric     | Unique identifier for each order                                |
| OrderDate        | Date        | Date the order was placed (2023-01-01 to 2023-03-31)            |
| CustomerID       | String      | Unique customer identifier                                      |
| Gender           | Categorical | Customer gender (Male, Female, Other)                           |
| Age              | Numeric     | Customer age (18–65)                                            |
| Region           | Categorical | Geographic region (North, South, East, West)                    |
| ProductCategory  | Categorical | Product category (Electronics, Clothing, Home & Kitchen, Books, Sports) |
| OrderAmount      | Numeric     | Total amount of the order in USD                                |
| PaymentMethod    | Categorical | Payment method (Credit Card, Paypal, Debit Card)                |

## Example Analysis Questions

1. What are the sales trends over time, and do they differ by region?
2. How do customer demographics (age, gender) relate to average order amount?
3. Which product categories have the highest sales, and what payment methods are most popular for each?

## Usage

- Use `generate_ecommerce_data.py` to regenerate the dataset.
- Analyze with Python (pandas, matplotlib, seaborn) or R (tidyverse, ggplot2).

## Portfolio Narrative Example

*"Analyzed 800 e-commerce transactions to uncover regional sales trends, demographic purchasing behaviors, and payment preferences. Identified that the West region consistently achieved higher order values, and electronics and home goods categories performed best. My analysis guided targeted marketing strategies, resulting in improved campaign ROI and more effective inventory planning."*
