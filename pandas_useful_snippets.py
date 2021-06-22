# Drop duplicates based on a column
df.drop_duplicates(subset=['column_foo'], inplace=True)

# Drop rows based on some condition
df.drop(df['column_foo'].isnull().index, inplace=True)
