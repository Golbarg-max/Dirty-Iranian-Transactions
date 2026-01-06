# Transaction Data Analysis

## Overview
Analysis of 10,000 Iranian transaction records to identify patterns in success rates, card type performance, and geographic trends using Python, MySQL, and data visualization.

## Technologies Used
- **Python**: pandas, matplotlib
- **MySQL**: Database design, complex queries
- **Jupyter Notebook**: Analysis documentation

## Dataset
- 10,000 transaction records from Kaggle
- Features: status, timestamp, card type, city, transaction amount
- Data quality issues: inconsistent naming, missing values, duplicate IDs

## Key Findings
- Overall transaction success rate: 46.34%
- Tehran accounts for 35% of all transactions
- Amex had the highest success rate between cards with 46.71% success rate

## Project Highlights
- **Data Cleaning**: Standardized inconsistent values across multiple columns using pandas
- **Database Design**: Created normalized MySQL schema and loaded 10K records
- **SQL Analysis**: Complex queries with JOINs, GROUP BY, CASE statements
- **Visualization**: Created charts to communicate insights

## Interactive Dashboard
- View the interactive Tableau dashboard: [Link](https://public.tableau.com/app/profile/golbarg.ghazinour/viz/TransactionAnalysisDashboard_17674947313660/Dashboard1?publish=yes)

## Files
- `iranian_transaction_analysis.ipynb` - Main analysis notebook
- `trx-10k.csv` - Raw transaction data
- `iranian_transaction_analysis.html` - Exported notebook
- `transactions_clean.csv` - Cleaned data [Link](https://public.tableau.com/app/profile/golbarg.ghazinour/viz/TransactionAnalysisDashboard_17674947313660/Dashboard1?publish=yes)
- Tableau Dashboard - 


## Future Improvements
- Time-series analysis of transaction patterns
- Predictive modeling for transaction success
- Interactive dashboard
