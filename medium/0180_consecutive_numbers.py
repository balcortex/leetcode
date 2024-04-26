import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # Sort by id (just in case)
    logs = logs.sort_values(by="id")

    # diff() compare the actual and the previous row,
    # if the two row are equal, then the result of diff() is zero
    # Also, check the first and the third row to be equal with diff(2).
    # The last two conditions checks that no number is missing between rows
    idx = (
        (logs.num.diff() == 0)
        & (logs.num.diff(2) == 0)
        & (logs.id.diff() == 1)  # No index missing between row 1 and 2
        & (logs.id.diff(2) == 2)  # No index missing between row 1 and 3
    )

    return (
        logs[idx][["num"]]
        .drop_duplicates()
        .reset_index(drop=True)  # do not insert the index into columns
        .rename(columns={"num": "ConsecutiveNums"})
    )


data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pd.DataFrame(data, columns=["id", "num"]).astype({"id": "int64", "num": "int64"})
output = consecutive_numbers(logs)
expected = pd.DataFrame({"ConsecutiveNums": [1]})
assert pd.DataFrame.equals(output, expected)


data = [[1, 1], [2, 1], [4, 1], [5, 1], [6, 2], [7, 1]]
logs = pd.DataFrame(data, columns=["id", "num"]).astype({"id": "int64", "num": "int64"})
output = consecutive_numbers(logs)
expected = pd.DataFrame({"ConsecutiveNums": []}).astype({"ConsecutiveNums": "int64"})
assert pd.DataFrame.equals(output, expected)
