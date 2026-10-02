import pandas as pd
import numpy as np
companies = pd.read_excel(r"C:\Users\pc\Downloads\companies_table.xlsx")
esgscores = pd.read_excel(r"C:\Users\pc\Downloads\ESG_scores.xlsx")
returns = pd.read_excel(r"C:\Users\pc\Downloads\Returns_table.xlsx")
print(returns.head(5))

companies.dropna(inplace=True)
esgscores.dropna(inplace=True)
returns.dropna(inplace=True)
