import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    # Get the maximum salary for each department
    # Transform outputs a pd.series the same length as the original dataframe
    max_by_deparment = employee.groupby("departmentId")["salary"].transform("max")

    # Get the indices where the actual salary of each employee is equal to that of the max
    mask = employee.salary == max_by_deparment

    # Merge the masked employee dataframe with the department dataframe
    df_merged = pd.merge(
        employee[mask], department, how="left", left_on="departmentId", right_on="id"
    )

    # Select only the required columns and re-index
    df_merged = df_merged[["name_y", "name_x", "salary"]].reset_index(drop=True)

    # Rename the columns and return
    return df_merged.rename(
        columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    )


data = [
    [1, "Joe", 70000, 1],
    [2, "Jim", 90000, 1],
    [3, "Henry", 80000, 2],
    [4, "Sam", 60000, 2],
    [5, "Max", 90000, 1],
]
employee = pd.DataFrame(data, columns=["id", "name", "salary", "departmentId"]).astype(
    {"id": "Int64", "name": "object", "salary": "Int64", "departmentId": "Int64"}
)
data = [[1, "IT"], [2, "Sales"]]
department = pd.DataFrame(data, columns=["id", "name"]).astype(
    {"id": "Int64", "name": "object"}
)
output = department_highest_salary(employee, department)

data = [["IT", "Jim", 90000], ["Sales", "Henry", 80000], ["IT", "Max", 90000]]
expected = pd.DataFrame(data, columns=["Department", "Employee", "Salary"]).astype(
    {"Department": "object", "Employee": "object", "Salary": "Int64"}
)
assert pd.DataFrame.equals(output, expected)
