import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Group by email and count the instances
    # `as_index = False` keeps the group as a column rather than an index
    # the count is stored in the column named `id`
    df_count = person.groupby("email", as_index=False).count()

    # Get the duplicated emails (count >= 2)
    duplicated = df_count[df_count["id"] > 1]

    # Return a pd.dataframe (using [[]])
    return duplicated[["email"]].rename(columns={"email": "Email"})


data = [[1, "a@b.com"], [2, "c@d.com"], [3, "a@b.com"]]
person = pd.DataFrame(data, columns=["id", "email"]).astype(
    {"id": "Int64", "email": "object"}
)
output = duplicate_emails(person)
expected = pd.DataFrame({"Email": ["a@b.com"]})
assert pd.DataFrame.equals(output, expected)
