import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Group by customer_orders and count occurrences
    num_orders = orders.groupby("customer_number").count().reset_index()

    # Get the mask where the (count of) order_number == the max
    mask = num_orders["order_number"] == num_orders["order_number"].max()

    # Get the customers using the mask, and return as dataframe
    return num_orders[mask][["customer_number"]].reset_index(drop=True)


data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=["order_number", "customer_number"]).astype(
    {"order_number": "Int64", "customer_number": "Int64"}
)
output = largest_orders(orders)
expected = pd.DataFrame({"customer_number": [3]}).astype({"customer_number": "Int64"})
assert pd.DataFrame.equals(output, expected)
