import pandas as pd

conditions = ["confirmed", "death", "recovered"]


daily_df = pd.read_csv("./data/daily_report.csv")
global_df = daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
global_df = global_df.rename(columns={"index": "condition"})

print(global_df)

# 나라별로 그룹핑 해보자

country_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
country_df = country_df.groupby("Country_Region")
country_df = country_df.sum().reset_index()
print(country_df)


# 필요한 데이터만 취하고.. 합을 내자.
""" => 함수로 옮김. 
import pandas as pd
df = pd.read_csv("./data/time_confirmed.csv")
df = df.drop(["Province/State","Country/Region","Lat", "Long"], axis=1).sum().reset_index(name="total")
df=df.rename(columns={"index":"date"})
df
"""


def make_global_df():
    def make_df(condition):
        df = pd.read_csv(f"./data/time_{condition}.csv")
        df = (
            df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1)
            .sum()
            .reset_index(name=condition)
        )
        df = df.rename({"index": "date"})
        return df

    final_df = None

    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df

        else:
            final_df = final_df.merge(condition_df)
        print(final_df)


# 나라별 일일 코로너 현황


def make_country_df(name):
    def make_df(condition):
        df = pd.read_csv(f"data/time_{condition}.csv")
        df = df.loc[df["Country/Region"] == name]
        df = (
            df.drop(columns=["Province/State", "Country/Region", "Lat", "Long"])
            .sum()
            .reset_index(name=condition)
        )
        df = df.rename(columns={"index": "date"})
        print(df)
        return df

    final_df = None

    for condition in conditions:
        condition_df = make_df(condition)

        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
        print(final_df)
    return final_df


g_df = make_global_df()
c_df = make_country_df("Afghanistan")
