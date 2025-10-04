# E‑commerce Sales Data Analysis Project

This repository contains a complete, self‑contained example of generating, exploring, and visualizing a synthetic e‑commerce sales dataset.  The project uses both Python and R to demonstrate typical tasks in a data analysis pipeline: data creation, cleaning, exploration, and visualization.

## Overview

The goal of this project is to showcase how to build a small, reproducible workflow for e‑commerce transaction data.  It begins by programmatically generating a dataset of 800 synthetic orders spanning the first quarter of 2023.  The dataset includes demographic attributes (age, gender, region) and transactional fields (order amount, product category, payment method).  Once the data are generated, the project provides two analysis pathways:

1. **Python analysis** via a Jupyter notebook (`notebooks/ecommerce_data_analysis.ipynb`), which cleans the data and produces exploratory charts using `pandas`, `matplotlib`, and `seaborn`.
2. **R analysis** via an R Markdown document (`reports/ecommerce_data_analysis.Rmd`), which performs similar analyses and creates comparable visualizations using `dplyr`, `ggplot2`, and `tidyr`.

All generated charts are saved to the `visualizations/` directory when the notebooks or R Markdown file are executed.

## Dataset Generation

The dataset is created by the Python script located at `scripts/generate_ecommerce_data.py`.  This script uses only built‑in Python modules (`random`, `datetime`, and `csv`) to avoid external dependencies.  Running the script will generate a CSV file at `data/ecommerce_sales_data.csv` with the following columns:

- `OrderID` – a unique integer identifier starting at `10001`.
- `OrderDate` – a date between 2023‑01‑01 and 2023‑03‑31.
- `CustomerID` – an anonymous customer identifier (e.g., `CUST001`).
- `Gender` – randomly chosen from “Male”, “Female”, and “Other”.
- `Age` – random age between 18 and 65.
- `Region` – one of “North”, “South”, “East”, or “West”.
- `ProductCategory` – one of “Electronics”, “Clothing”, “Home & Kitchen”, “Books”, or “Sports”.
- `OrderAmount` – a floating‑point number representing the transaction amount, drawn from reasonable price ranges per product category.
- `PaymentMethod` – one of “Credit Card”, “Paypal”, or “Debit Card”.

To regenerate the dataset (optional, since it’s already included), run the script from the project root:

```bash
python scripts/generate_ecommerce_data.py
```

The script automatically writes the CSV to the `data/` directory, creating it if necessary.  Because the random number generator is seeded, running the script will always produce the same dataset.

## Directory Structure

The repository is organized as follows:

```
.
├── data/
│   └── ecommerce_sales_data.csv       # Generated dataset of 800 orders
├── scripts/
│   └── generate_ecommerce_data.py     # Generates the synthetic dataset
├── notebooks/
│   └── ecommerce_data_analysis.ipynb   # Python Jupyter notebook for analysis
├── reports/
│   └── ecommerce_data_analysis.Rmd     # R Markdown document for analysis
├── visualizations/
│   └── (created charts saved here by the analyses)
├── requirements.txt                    # Python libraries needed for the notebook
└── README.md                           # This file
```

The `visualizations/` directory will be populated when you run either analysis; the repository does not include any pre‑generated images to keep it lightweight.

## Python Analysis

The Jupyter notebook in `notebooks/ecommerce_data_analysis.ipynb` performs the following steps:

1. **Load the dataset** using `pandas` and parse the `OrderDate` column as a date.
2. **Inspect and clean** the data (verify types, check for missing values).
3. **Visualize** sales trends over time, average order amounts by region, sales by product category and payment method (heatmap), and the relationship between customer age and order amount.
4. **Save plots** to the `visualizations/` folder.

To run the notebook:

1. Install the Python dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

2. Launch Jupyter and open the notebook:

   ```bash
   jupyter notebook notebooks/ecommerce_data_analysis.ipynb
   ```

3. Run the cells to execute the analysis.  The resulting figures will appear inline and be saved to the `visualizations/` directory.

## R Analysis

The R Markdown document in `reports/ecommerce_data_analysis.Rmd` mirrors the Python analysis using the R ecosystem.  It reads the same CSV dataset, performs summary statistics, generates comparable charts with `ggplot2`, and saves them to the `visualizations/` directory.

To run the R analysis:

1. Make sure you have the `tidyverse` packages installed (e.g., via `install.packages('tidyverse')`) along with `RColorBrewer`.
2. Open the R Markdown file in RStudio.
3. Knit the document to an HTML report or run individual chunks.  Charts will be created in the `visualizations/` directory.

## Reproducibility and Customization

The random number generator in the data generation script is seeded to ensure that the synthetic dataset is identical every time it is generated.  If you wish to create a different dataset, you can change or remove the seeding in `scripts/generate_ecommerce_data.py` (look for the `random.seed(42)` line).  You can also adjust the `n_rows` constant or the price ranges to produce datasets of different sizes or characteristics.

## License

This project is provided for demonstration and educational purposes.  Feel free to use or modify the code as needed for your own projects.