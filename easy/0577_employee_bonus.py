import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Merge employee and bonus dataframes
    # We need all employes names, so is a left join
    df_merged = employee.merge(bonus, how="left", left_on="empId", right_on="empId")

    # Get the values smaller than 1000, or the missing values
    mask = (df_merged.bonus < 1000) | (df_merged.bonus.isna())

    return df_merged[mask][["name", "bonus"]].reset_index(drop=True)


data = [
    [3, "Brad", None, 4000],
    [1, "John", 3, 1000],
    [2, "Dan", 3, 2000],
    [4, "Thomas", 3, 4000],
]
employee = pd.DataFrame(data, columns=["empId", "name", "supervisor", "salary"]).astype(
    {"empId": "Int64", "name": "object", "supervisor": "Int64", "salary": "Int64"}
)
data = [[2, 500], [4, 2000]]
bonus = pd.DataFrame(data, columns=["empId", "bonus"]).astype(
    {"empId": "Int64", "bonus": "Int64"}
)
output = employee_bonus(employee, bonus)
expected_data = [["Brad", None], ["John", None], ["Dan", 500]]
expected = pd.DataFrame(expected_data, columns=["name", "bonus"]).astype(
    {"name": "object", "bonus": "Int64"}
)
assert pd.DataFrame.equals(output, expected)
