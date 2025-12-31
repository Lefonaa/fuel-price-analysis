# South African Fuel Price Trend Analysis (2023 - 2024)

## Project Overview
This project provides a statistical analysis of Petrol and Diesel price fluctuations in South Africa from January 2023 to May 2024. As a 3rd-year Data Science student, I developed this tool to demonstrate practical skills in data wrangling, trend visualization, and statistical reporting.

## Technical Stack
* **Language:** Python
* **Libraries:** Pandas (Data manipulation), Matplotlib & Seaborn (Visualizations)

## Data Cleaning & Preparation
The raw dataset (`petrolprices.csv`) contained monthly records with semicolon (;) delimiters.
* **Handling Null Values:** The original data included `0.0` values for June – December 2024. 
* **Wrangling:** Using Python, I filtered these entries to ensure the final analysis and visualizations only reflected verified data points from Jan 2023 to May 2024, preventing statistical skew.

## Visualizations & Insights
Below are the key visual reports generated from the dataset:

### 1. Overall Price Trends
![Price Trends Over Time](Screenshot%202025-12-31%20173301.png)
*Observations on the general upward or downward movement of fuel costs.*

### 2. Petrol vs. Diesel Comparison
![Comparison Chart](Screenshot%202025-12-31%20173337.png)
*Analyzing the price gap between Petrol and Diesel during high-volatility months.*

### 3. Price Distribution & Volatility
![Volatility Plot](Screenshot%202025-12-31%20173346.png)
![Monthly Variations](Screenshot%202025-12-31%20173355.png)

## Key Findings
* **2023 Peak:** Prices reached a significant peak in October 2023, with Petrol at 24.86 and Diesel at 25.98.
* **Market Trends:** Diesel consistently maintained a higher price point than Petrol throughout most of 2023, following global supply chain trends.

---
**Author:** Lefona Moloi
**Education:** BSc Information Technology (Data Science) | Eduvos
