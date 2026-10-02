##### **Project Summary \& Output — ESG Factor Return Analysis**



***Question: Do companies with the highest ESG scores deliver higher returns than those with the lowest — is there an "ESG premium"?***



Data: 15 large Indian companies (NIFTY constituents), one year (2024). Per firm: ESG score, sector, market cap, and annual return are loaded from three tables (companies, esgscores, returns) and joined into one analysis table in SQLite3.



***Methods and Workflow***



Merged the three tables on company ID.

Split firms into 5 quintiles by ESG score using pd.qcut (Q1 = lowest ESG, Q5 = highest).

Computed average return per quintile and the Q5–Q1 spread.

Ran a Pearson correlation between ESG score and returns.

Controlled for sector and size (market-cap), then ran a multiple regression: returns \~ esg + size + sector.



***Data Visualization***



ESG Score vs. Returns — scatter with regression line (downward slope)

Returns by Quintile — boxplot of return distribution per group

ESG–Return by Sector — faceted regression plots

Average Return by Quintile — bar chart

The finding is, worst-ESG firms outperformed best-ESG firms. The Q5–Q1 spread was –30.5%, and the overall correlation was negative and significant: r = –0.54, p = 0.038.



Average returns fall from Q1 (18%) to Q5 (–12%), driven largely by high-ESG IT firms (TCS, Infosys) that had a weak 2024. Within-sector correlations were weak and insignificant, and the regression showed ESG did not independently predict returns once sector and size were controlled for.



***Conclusion:*** In this dataset, there is no ESG premium — higher ESG scores did not translate into higher returns. The negative relationship appears driven more by sector and timing than by ESG itself.



***Caveat:*** Small sample (15 firms, one year) — results are indicative, not conclusive. The negative spread is heavily influenced by a single sector's bad year, and within-sector tests lacked statistical power. A larger, multi-year sample with risk-adjusted returns would be needed to confirm whether the ESG–return link is real or an artifact of sector and timing.

