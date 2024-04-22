import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Make self-join (inner join) to have the employee and manager salaries
    # on the same row
    df = employee.merge(employee, how="inner", left_on="managerId", right_on="id")

    # Get the mask of the employees (salary_x) who earn more than the managers
    # (salary_y), and use it to retrieve the employees ('name_x')
    emp = df[df["salary_x"] > df["salary_y"]]["name_x"]

    # Now we have a pd.series, and we are asked to return a pd.dataframe with
    # a column named 'Employee'
    return pd.DataFrame({"Employee": emp})


data = [
    [1, "Joe", 70000, 3],
    [2, "Henry", 80000, 4],
    [3, "Sam", 60000, None],
    [4, "Max", 90000, None],
]
employee = pd.DataFrame(data, columns=["id", "name", "salary", "managerId"]).astype(
    {"id": "Int64", "name": "object", "salary": "Int64", "managerId": "Int64"}
)
output = find_employees(employee)
expected = pd.DataFrame({"Employee": ["Joe"]})
assert pd.DataFrame.equals(output, expected)

data = [
    [1, "Joe", 70000, 3],
    [2, "Henry", 800000, 4],
    [3, "Sam", 60000, None],
    [4, "Max", 90000, None],
]
employee = pd.DataFrame(data, columns=["id", "name", "salary", "managerId"]).astype(
    {"id": "Int64", "name": "object", "salary": "Int64", "managerId": "Int64"}
)
output = find_employees(employee)
expected = pd.DataFrame({"Employee": ["Joe", "Henry"]})

assert pd.DataFrame.equals(output, expected)
