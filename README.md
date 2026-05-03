# 🌸 Baku Spring Temperature Analysis (2005-2026)

## Project Overview
This project analyzes historical temperature data from Baku to identify trends in spring weather patterns. As a self-taught data analyst, I built this to practice data cleaning with **Pandas**, trend visualization with **Matplotlib**, and mathematical modeling with **Numpy**.

## The reason why I did this project
It is my first data analysis project. I honestly did it because despite it being May 3rd, I am wearing a sweater. I wanted to see if springs actually got colder here or is it just my bias.
I enjoyed doing it!

## The Data
The dataset includes daily temperature recordings from 2005 through 2026. 
* **Source:** baku_2005_2026.csv is taken from meteoblue.com
* **Key Columns:** Date, Temperature (°C)

## Key Insights
While the "wiggly jiggly" raw data shows high variance, the trendlines reveal something fascinating:
* **Full Spring (Mar-May):** The overall average temperature remains relatively stable at around 11°C.
* **Late Spring (Apr-May):** There is a visible downward slope, suggesting that April and May are getting slightly cooler over the years.
* **The "March Effect":** Because the overall spring trend is flat while late spring is cooling, it implies that **March temperatures in Baku are actually rising** to balance the average!

## Technologies Used
* **Python**
* **Pandas** (Data Manipulation & Grouping)
* **Numpy** (Linear Regression/Trendlines)
* **Matplotlib** (Data Visualization)

## How to Run
1. Clone the repo.
2. Ensure you have `pandas`, `numpy`, and `matplotlib` installed.
3. Run `python baku_analysis.py`.
