import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", ascending=True, inplace=True)
    person.drop_duplicates(subset="email", inplace=True)
    person.reset_index(inplace=True, drop=True)


data = [[1, "john@example.com"], [2, "bob@example.com"], [3, "john@example.com"]]
person = pd.DataFrame(data, columns=["id", "email"])
expected = pd.DataFrame(
    {"id": [1, 2], "email": ["john@example.com", "bob@example.com"]}
)
delete_duplicate_emails(person)
assert pd.DataFrame.equals(person, expected)

data = [[2, "abc@efg.com"], [1, "abc@efg.com"]]
person = pd.DataFrame(data, columns=["id", "email"])
expected = pd.DataFrame({"id": [1], "email": ["abc@efg.com"]})
delete_duplicate_emails(person)
assert pd.DataFrame.equals(person, expected)
