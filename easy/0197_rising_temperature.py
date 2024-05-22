import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # First order by day
    weather = weather.sort_values(by="recordDate")

    # Compare the two contiguos rows,
    # the difference between days must be 1,
    # the temperature must be greater than 0
    mask = (weather["recordDate"].diff().dt.days == 1) & (
        weather["temperature"].diff() > 0
    )

    return weather[mask][["id"]].reset_index(drop=True)


data = [
    [1, "2015-01-01", 10],
    [2, "2015-01-02", 25],
    [3, "2015-01-03", 20],
    [4, "2015-01-04", 30],
]
weather = pd.DataFrame(data, columns=["id", "recordDate", "temperature"]).astype(
    {"id": "Int64", "recordDate": "datetime64[ns]", "temperature": "Int64"}
)
output = rising_temperature(weather)
expected = pd.DataFrame({"id": [2, 4]}).astype({"id": "Int64"})
assert pd.DataFrame.equals(expected, output)

data = []
weather = pd.DataFrame(data, columns=["id", "recordDate", "temperature"]).astype(
    {"id": "Int64", "recordDate": "datetime64[ns]", "temperature": "Int64"}
)
output = rising_temperature(weather)
expected = pd.DataFrame({"id": []}).astype({"id": "Int64"})
assert pd.DataFrame.equals(expected, output)
