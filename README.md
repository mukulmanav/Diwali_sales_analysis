# 🛍️ Exploratory Data Analysis (EDA) - Diwali Sales Analysis

## 📌 Objective
This project aims to **improve customer experience** and **increase revenue** by analyzing Diwali sales data. Through Exploratory Data Analysis (EDA), key trends and patterns in customer purchasing behavior are identified to help businesses make data-driven decisions.

## 📊 Dataset Overview
The dataset contains transactional data from Diwali sales, including customer demographics, product details, and sales amounts. The key columns in the dataset are:

- **Gender**: Male/Female
- **Age Group**: Age category of customers
- **State**: Customer’s location
- **Marital Status**: Whether the customer is married
- **Occupation**: Job sector of the customer
- **Product Category**: Type of product purchased
- **Product ID**: Unique product identifier
- **Orders**: Number of items ordered
- **Amount**: Total purchase amount

## 🔍 Key Analyses Performed

### 1️⃣ **Data Cleaning & Preparation**
- Removed unnecessary columns (`Status`, `unnamed1`).
- Handled missing values by dropping rows with `NaN`.
- Converted `Amount` column from float to integer for consistency.
- Renamed columns for better readability.

### 2️⃣ **Customer Demographics Analysis**
- **Gender Analysis**: Distribution of male vs. female customers.
- **Age Group Analysis**: Analyzed sales contributions across different age groups.
- **Marital Status Analysis**: Evaluated purchase behavior based on marital status.
- **State-wise Analysis**: Identified top-performing states in terms of sales and number of orders.

### 3️⃣ **Sales & Revenue Analysis**
- **Total Orders per State**: Identified states with the highest number of purchases.
- **Total Sales per State**: Determined which states contributed the most to revenue.
- **Occupation-based Analysis**: Found which job sectors contributed the highest revenue.
- **Product Category Analysis**: Analyzed which product categories drive the most sales.
- **Top Selling Products**: Identified the best-selling products based on the number of orders.

## 📈 Visualizations
- **Bar Plots**: Used to display sales trends by gender, age, state, and occupation.
- **Count Plots**: Analyzed distribution of purchases across categories.
- **Histograms**: Examined the spread of numerical features.

## 🏆 Conclusion
- **Married women aged 26-35** from **Uttar Pradesh, Maharashtra, and Karnataka** working in **IT, Healthcare, and Aviation** are the most likely to make purchases.
- **Food, Clothing, and Electronics** are the most purchased product categories.
- State-wise, **Uttar Pradesh, Maharashtra, and Karnataka** generated the highest revenue.

