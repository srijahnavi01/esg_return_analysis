import sqlite3
import pandas as pd 
from scipy import stats
import statsmodels.api as sm

conn = sqlite3.connect("esg.db")  
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS returns (
    date       TEXT,
    ticker     TEXT,
    esg_score  REAL,
    return_pct REAL
);
""")

conn.commit()

df = pd.read_excel(r"C:\Users\pc\Downloads\Returns_table.xlsx")
df.to_sql("returns", conn, if_exists="replace", index=False)

print(pd.read_sql("SELECT * FROM returns LIMIT 5;", conn))
conn.close()

import pandas as pd
import sqlite3

conn = sqlite3.connect("esg.db")

companies = pd.read_excel(r"C:\Users\pc\Downloads\companies_table.xlsx")
esgscores = pd.read_excel(r"C:\Users\pc\Downloads\ESG_scores.xlsx")
returns   = pd.read_excel(r"C:\Users\pc\Downloads\Returns_table.xlsx")

companies.to_sql("companies", conn, if_exists="replace", index=False)
esgscores.to_sql("esgscores", conn, if_exists="replace", index=False)
returns.to_sql("returns", conn, if_exists="replace", index=False)

query = """
    select c.company_id, c.company_name, c.sector, e.esg_score, e.year,r.returns_pct
    from companies c
    left join esgscores e on c.company_id = e.company_id
    left join returns r on c.company_id = r.company_id
    """

df = pd.read_sql(query, conn)
print(df)

df = df.dropna(subset=['esg_score', "returns_pct"])

df= df.sort_values(by="esg_score")
print(df)

df["quintile"] = pd.qcut(df["esg_score"], 5, labels = [1,2,3,4,5])
avg_returns = df.groupby("quintile")["returns_pct"].mean()
print(avg_returns)
print(avg_returns.index)

print(df[["Company_Name", "esg_score", "returns_pct"]].sort_values("esg_score").head())

q1 = avg_returns.loc[1]   
q5 = avg_returns.loc[5]   
spread = q5 - q1
print(f"Q5 - Q1 = {spread:.4f}")

if spread > 0:
    print("Best-ESG outperforms worst-ESG")
elif spread < 0:
    print("Worst-ESG outperforms best-ESG")
else:
    print("No difference")

r, p = stats.pearsonr(df["esg_score"], df["returns_pct"])
print(f"Overall: r = {r:.4f}, p = {p:.4f}")

for sector, grp in df.groupby("Sector"):
    if len(grp) >= 3:
        r, p = stats.pearsonr(grp["esg_score"], grp["returns_pct"])
        print(f"{sector}: r = {r:.4f}, p = {p:.4f} (n={len(grp)})")

print(df.columns.tolist())
df = pd.merge(df, companies[["Company_ID", "Market_Cap_INR_Cr"]], on="Company_ID", how="left")

df_reg = pd.get_dummies(df, columns=["Sector"], drop_first=True)

X = df_reg[["esg_score", "Market_Cap_INR_Cr"] + [c for c in df_reg.columns if c.startswith("Sector_")]]
X = sm.add_constant(X)          
y = df_reg["returns_pct"]

model = sm.OLS(y, X).fit()
print(model.summary())
