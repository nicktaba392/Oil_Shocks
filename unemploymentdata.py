import pandas as pd
from datetime import date
from calendar import monthrange

df = pd.read_csv("data_average.csv")
print(df.head())

# df['date'] = None
# date_of_last_day_of_quarter = date(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])

df["date"] = None


# adding the last date of the quarter
for i in range(len(df)):
    year = df["Year"][i]
    quarter = df["Quarter"][i]
    last_month_of_quarter = quarter * 3
    last_date = date(
        year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1]
    )
    df["date"][i] = last_date
df["date"] = pd.to_datetime(df["date"])

# print(df.head(10))
# df.to_csv("unemployment_quarterly_completed.csv")


df_main = pd.read_csv("df_completed.csv")
df_main["CLOSDATE"] = pd.to_datetime(df_main["CLOSDATE"])
# print(df_main.head(10))

print(df_main.head())

new_df = pd.merge(
    left=df_main,
    right=df,
    how="left",
    left_on=["CLOSDATE", "STATE_US"],
    right_on=["date", "State"],
)

# new_df.to_csv("new_df.csv")
print(new_df.head())

print(len(df_main))

new_df = new_df.dropna()
print(len(new_df))

new_df.to_csv("df_completed2.csv")
