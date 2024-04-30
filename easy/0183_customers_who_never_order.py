import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge both tables to have each customer with their order
    df = customers.merge(orders, how="left", left_on="id", right_on="customerId")

    # Get a mask indicating where the order values are None
    mask = df.customerId.isna()

    # Index the merged df using the mask and return the specific columns
    return (
        df[mask][["name"]].reset_index(drop=True).rename(columns={"name": "Customers"})
    )


data = [[1, "Joe"], [2, "Henry"], [3, "Sam"], [4, "Max"]]
customers = pd.DataFrame(data, columns=["id", "name"]).astype(
    {"id": "Int64", "name": "object"}
)
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=["id", "customerId"]).astype(
    {"id": "Int64", "customerId": "Int64"}
)

output = find_customers(customers, orders)
expected = pd.DataFrame({"Customers": ["Henry", "Max"]})
assert pd.DataFrame.equals(output, expected)


data = [[5, "wyu{sk"], [2, "rgt"], [4, "hbrmrz"], [1, "tmjow"], [3, "ynrl{wq"]]
customers = pd.DataFrame(data, columns=["id", "name"]).astype(
    {"id": "Int64", "name": "object"}
)
data = [[10, 4], [3, 5], [2, 3], [6, 2], [4, 3], [8, 3], [9, 3], [1, 2], [7, 2], [5, 3]]
orders = pd.DataFrame(data, columns=["id", "customerId"]).astype(
    {"id": "Int64", "customerId": "Int64"}
)
output = find_customers(customers, orders)
expected = pd.DataFrame({"Customers": ["tmjow"]})
assert pd.DataFrame.equals(output, expected)
