# Drop duplicates based on a column
df.drop_duplicates(subset=['column_foo'], inplace=True)

# Drop rows based on some condition
df.drop(df[df['column_foo'].isnull() ==True].index, inplace=True)


# To print a single row values for debugging when there is a large number of columns (e.g 100 columns) 
df.iloc[0].T.values
