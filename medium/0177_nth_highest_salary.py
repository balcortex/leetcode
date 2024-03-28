import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Just keep unique salaries
    salaries = employee.drop_duplicates(subset=["salary"])

    # Sort by highest to lowest salary
    salaries = salaries.sort_values(by="salary", ascending=False)

    # Get the salary at index [N - 1] (0-based index)
    # If there are enough values
    # Negative indices are not supported either
    if len(salaries) < N or N < 1:
        n_high = None
    else:
        n_high = salaries.salary.iloc[N - 1]

    return pd.DataFrame({f"getNthHighestSalary({N})": [n_high]})


data = [[1, 100], [2, 100], [3, 200], [4, 300], [5, 300]]
employee = pd.DataFrame(data, columns=["id", "salary"]).astype(
    {"id": "Int64", "salary": "Int64"}
)

expected = pd.DataFrame({"getNthHighestSalary(2)": [200]})
output = nth_highest_salary(employee, 2)
assert pd.DataFrame.equals(expected, output) is True

expected = pd.DataFrame({"getNthHighestSalary(1)": [300]})
output = nth_highest_salary(employee, 1)
assert pd.DataFrame.equals(expected, output) is True

expected = pd.DataFrame({"getNthHighestSalary(5)": [None]})
output = nth_highest_salary(employee, 5)
assert pd.DataFrame.equals(expected, output) is True
