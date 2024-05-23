import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Sort by player_id and then by event_date
    activity = activity.sort_values(by=["player_id", "event_date"])

    # Keep the first duplicate only
    activity = activity.drop_duplicates(subset="player_id")

    return (
        activity[["player_id", "event_date"]]
        .rename(columns={"event_date": "first_login"})
        .reset_index(drop=True)
    )


data = [
    [1, 2, "2016-03-01", 5],
    [1, 2, "2016-05-02", 6],
    [2, 3, "2017-06-25", 1],
    [3, 1, "2016-03-02", 0],
    [3, 4, "2018-07-03", 5],
]
activity = pd.DataFrame(
    data,
    columns=["player_id", "device_id", "event_date", "games_played"],
).astype(
    {
        "player_id": "Int64",
        "device_id": "Int64",
        "event_date": "datetime64[ns]",
        "games_played": "Int64",
    }
)
output = game_analysis(activity)
data2 = [
    [1, "2016-03-01"],
    [2, "2017-06-25"],
    [3, "2016-03-02"],
]
expected = pd.DataFrame(data2, columns=["player_id", "first_login"]).astype(
    {
        "player_id": "Int64",
        "first_login": "datetime64[ns]",
    }
)
assert pd.DataFrame.equals(output, expected)
