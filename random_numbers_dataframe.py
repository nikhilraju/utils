import pandas as pd
import numpy as np
import random

# Create a Dataframe with 100 rows and 4 columns with integer values between 0 and 100
# Add dtype = dtype=pd.Int64Dtype() to allow Nullable integer values ( these are pandas integers as 
# opposed to numpy integers)
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), dtype=pd.Int64Dtype())

# Replace ~10% of the values with Numpy NaN values
ix = [(row, col) for row in range(test_df.shape[0]) for col in range(test_df.shape[1])]
for row, col in random.sample(ix, int(round(.1*len(ix)))):
    test_df.iat[row, col] = np.nan

