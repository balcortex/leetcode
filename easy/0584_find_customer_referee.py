import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Find the indeces where referee_id is null or different from 2
    mask = (customer.referee_id != 2) | (customer.referee_id.isna())

    # Apply the mask, select the required columns and re-index
    return customer[mask][["name"]].reset_index(drop=True)


data = [
    [1, "Will", None],
    [2, "Jane", None],
    [3, "Alex", 2],
    [4, "Bill", None],
    [5, "Zack", 1],
    [6, "Mark", 2],
]
customer = pd.DataFrame(data, columns=["id", "name", "referee_id"]).astype(
    {"id": "Int64", "name": "object", "referee_id": "Int64"}
)
output = find_customer_referee(customer)
expected = pd.DataFrame({"name": ["Will", "Jane", "Bill", "Zack"]})
assert pd.DataFrame.equals(output, expected)
