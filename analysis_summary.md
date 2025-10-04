## E‑commerce Sales Data Analysis Summary

This summary distills the key findings from analysing an 800‑row synthetic e‑commerce transaction dataset in R.  The data cover orders placed between January and March 2023 and include customer demographics, order amounts, product categories and payment methods.

### Overall spending patterns

* **Total revenue:** The dataset represents approximately **\$106,849** in sales from **800 orders**, yielding an average order value of **\$133.56**.
* **Customer age:** Shoppers range from 18 to 65 years old, with an average age of about **42 years** and a median age of **43**.

### Regional behaviour

Orders are distributed fairly evenly across the four regions.  Customers in the **West** spend the most per transaction, averaging about **\$139** per order.  The **South** and **North** regions have slightly lower average order values (around **\$131–\$132**), while the **East** contributes the smallest share of total sales.

### Product mix

* **Electronics** dominate revenue, accounting for nearly **45 %** of sales.  Higher‑priced items in this category drive the overall average order value.
* **Home & Kitchen** products rank second with about **23 %** of revenue, followed by **Sports** gear (**19 %**), **Clothing** (**10 %**) and **Books** (**4 %**).

These proportions highlight where the business is currently strongest and suggest areas where there may be room to expand.

### Payment methods

* **Credit cards** are the preferred payment option, used in **487 orders** and generating roughly **\$65.7 k** in revenue.
* **PayPal** processes **239 orders** with **\$31.5 k** in revenue.
* **Debit cards** account for **74 orders** and **\$9.7 k** in sales.

The dominance of credit cards indicates customer comfort with this method, while PayPal serves as a meaningful secondary option.

### Customer demographics

Gender representation is nearly even, with **389 orders** placed by men and **381 orders** placed by women.  Average order values are also similar—around **\$132–\$134**—indicating no strong gender‑based differences in spending.  A small group identifying as “Other” (30 orders) spends more per order on average (about **\$145**), though the sample size is too small for firm conclusions.

### Sales timing

Daily sales fluctuate significantly.  The busiest day is **28 February 2023**, with about **\$2,816** in revenue, while **7 March 2023** is the quietest day at **\$280**.  Such variability suggests that promotional events or pay cycles could heavily influence purchasing behaviour.

### Age and spending

An analysis of the relationship between customer age and order amount yields a correlation coefficient of **0.05**, indicating **no meaningful linear relationship**.  In other words, older shoppers are not consistently spending more or less than younger shoppers.

### Takeaways

These synthetic data illustrate how transaction logs can reveal high‑value products, preferred payment methods, and regional or demographic trends.  In a real‑world setting, similar analyses can help e‑commerce teams fine‑tune marketing campaigns, manage inventory, and better understand customer behaviour.  Although this dataset is fictional, the methodology and insights can be directly applied to real transaction data to inform decision‑making.