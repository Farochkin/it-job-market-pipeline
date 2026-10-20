import pandas as pd

from datetime import datetime

timestamp = "2026-10-20 15:00:00"

dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

print(dt. type(dt))

df = pd.read_csv('data/jobs.csv')

# print(df.dtypes)

# print("\nFirst 5 jobs:")
# print(df.head(1))

# print("\nDataset shape:")
# print(df.shape)
# print(df['salary'] > 70000)

# print(df['salary'][df['salary'] > 70000])
# print(df[df['salary'] < 60000])
# print(df)
# print(df['salary'])

# print(df['salary'] > 70000)
# print(df['salary'][df['salary'] > 70000])
# print(df[df['salary'] > 70000])
# print(df[df['salary'] < 60000])

# print(df[df['salary'] > 70000])
# print(df['salary'] > 70000)

# print(df.dtypes)

# print(df.isna().sum())

# print("Total jobs:", df.shape[0])
# print("Missing salaries:", df["salary"].isna().sum())
# print("Average known salary:", df["salary"].mean())

# print(df.duplicated(subset=['title', 'company', 'location', 'salary']))
# clean_df = df.drop_duplicates(
#     subset=["title", "company", "location", "salary"]
# )
# print(df.shape[0] - clean_df.shape[0])
# print(clean_df['salary'].mean())
# print(df)


# clean_df = (
#     df.sort_values('updated_at')
#     .drop_duplicates(subset=['source',	'posting_id'], keep='last')
#     )


# print(clean_df)

# print(df.shape, clean_df.shape)
# print(df.duplicated(subset=["title", "company", "salary"]))
# df = df.drop_duplicates('title', 'company', 'location', 'salary', 'skills')
# print(df)

# timestamp = "2026-10-20 15:00:00"
# current = datetime.strptime(timestamp)