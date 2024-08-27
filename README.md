# IT Job Market Analysis in Poznań

This project aims to analyze the IT job market in Poznań using data collected from JustJoinIT. It consists of two main components:

1. **scrapper.py** - A Python script that scrapes job offers from [JustJoinIT Poznań](https://justjoin.it/poznan). This script collects information about job listings, including salary data and required skills, using web scraping techniques.

2. **JustJoinIT.ipynb** - A Google Colab notebook where data analysis is performed. The notebook includes:
   - Calculation of average salaries for junior and senior positions.
   - Determination of median, maximum, and minimum salaries.
   - Analysis of the most in-demand skills in the job market.

## Installation and Usage

1. **Install Required Libraries**:
   Ensure you have the necessary Python libraries installed. Use the following command to install them:
   ```bash
   pip install beautifulsoup4 pandas selenium
2. **Run the Data Scraping Script:** To collect data, execute the **scrapper.py** script
3. **Analyze Data:** Open **JustJoinIT.ipynb** in Google Colab, load the collected data, and perform the analysis.
