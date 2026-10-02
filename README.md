##### **ESG Factor Return Analysis**



A data-driven study examining whether companies with strong ESG scores deliver higher returns than those with weaker ESG performance  testing the widely discussed "ESG premium" hypothesis on a sample of large Indian companies.



***Overview***

This project brings together ESG scores, annual returns, and company fundamentals stored across three tables in a SQLite database. It merges them into a single analysis table, groups firms into ESG quintiles, and applies correlation and regression techniques to determine whether environmental, social, and governance performance is rewarded in the market.



***Structure and Work flow***



data\_cleaning.py:

Loads three different datasets into three different variables and checks if they are properly loaded, and if they have any redundant or missing values and cleans them accordingly



sql.py:

Loads the three source tables and joins them into one clean analysis table, performs Quintile analysis and Correlation and Controlling



charts.ipynb:

Perform various methods of data visualization using different charts and plots for a better and faster conclusion on return analysis





*The folder also consists of saved chart images in the png format for a clear picture of the conclusions*



***Charts***



\* ESG Score vs. Returns  scatter plot with a fitted regression line

\* Returns by Quintile  boxplot showing the distribution within each ESG group

\* ESGReturn Relationship by Sector  faceted regression plots per sector

\* Average Return by Quintile  bar chart comparing mean returns across groups

