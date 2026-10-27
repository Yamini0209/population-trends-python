# Population Trends Analysis (Python)

A Python data analysis project that cleans, reshapes, and visualizes population growth trends across selected countries (India, USA, China, Japan, Brazil, and Germany) from 1960 to 2020.

## 🚀 Features
* **Data Cleaning & Handling:** Generates a clean dataset, saves it to a CSV file, and checks for missing values using `pandas`.
* **Data Metrics:** Calculates population sizes in millions, tracks percentage changes, and identifies the fastest-growing countries.
* **Automated Plotting:** Generates and saves 6 distinct analysis charts into a dedicated output folder.

## 📊 Visualizations Created
The script automatically saves the following charts inside a `plots/` directory:
* **01_line_trend.png** - Historical population growth trajectories.
* **02_bar_2020.png** - Country-by-country population size comparison for 2020.
* **03_stacked_area.png** - Cumulative population growth totals over time.
* **04_growth_heatmap.png** - Grid display of population percentage change rates.
* **05_pie_share.png** - Percentage share of total combined population in 2020.
* **06_index_subplots.png** - Comparative individual growth scales (Base Year 1960 = 100).

## 🛠️ Libraries Used
* Python 3
* Pandas
* Numpy
* Matplotlib
