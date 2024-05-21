# https://leetcode.com/problems/rising-temperature/submissions/1251286810/

import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    if len(weather) == 0:
        return pd.DataFrame({"id": []})

    # Compare the two contiguos rows, if the value is greater than 0, keep the row
    weather = weather.sort_values(by="recordDate", ascending=True)
    mask = (weather["id"].diff() == 1) & (weather["temperature"].diff() > 0)

    # The first row has no previuos row, so it has the value of NaN
    # Change it to False, so the mask can be applied to the original dataframe
    mask.iloc[0] = False

    return weather[mask][["id"]]


data = [
    [1, "2015-01-01", 10],
    [2, "2015-01-02", 25],
    [3, "2015-01-03", 20],
    [4, "2015-01-04", 30],
]
weather = pd.DataFrame(data, columns=["id", "recordDate", "temperature"]).astype(
    {"id": "Int64", "recordDate": "datetime64[ns]", "temperature": "Int64"}
)
