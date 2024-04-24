import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Edge case, the dataframe is empty
    if scores.size == 0:
        return pd.DataFrame({"score": [], "rank": []})

    # Sort the scores by the column 'score' in descending order
    # We do not need the 'id' column
    scores = scores.sort_values(by="score", ascending=False).drop(columns="id")

    # Create a new dataset containing only the score duplicates
    df = (
        scores.drop_duplicates(subset="score")
        .reset_index()  # The first index isn't sorted, move it to a new column
        .reset_index()  # This index is sorted, we will use it to create a rank column
        .drop(columns="index")  # The first index we moved, drop it
        .rename(columns={"level_0": "rank"})  # Rename the second index to `rank`
    )

    df["rank"] = df["rank"] + 1  # The rank starts at zero, so add 1

    # Finally, we just need to left merge the `scores` and the `df`
    # to put the ranks on the `scores` dataframe
    return scores.merge(right=df, how="left", left_on="score", right_on="score")


data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=["id", "score"]).astype(
    {"id": "Int64", "score": "Float64"}
)
output = order_scores(scores)
expected = pd.DataFrame(
    {"score": [4.0, 4.0, 3.85, 3.65, 3.65, 3.5], "rank": [1, 1, 2, 3, 3, 4]}
).astype({"rank": "int64", "score": "Float64"})
assert pd.DataFrame.equals(output, expected)


data = []
scores = pd.DataFrame(data, columns=["id", "score"])
output = order_scores(scores)
expected = pd.DataFrame({"score": [], "rank": []})
assert pd.DataFrame.equals(output, expected)
