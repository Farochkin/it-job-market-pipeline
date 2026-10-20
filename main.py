import pandas as pd

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

print(df['salary'] > 70000)
print(df['salary'][df['salary'] > 70000])
print(df[df['salary'] > 70000])
print(df[df['salary'] < 60000])