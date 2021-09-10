import pandas as pd
import numpy as np
import random

test_df = pd.DataFrame(np.random.randint(0,100.0,size=(10, 4)), columns=['A','B','C','D'], dtype=pd.Int64Dtype())
ix = [(row, col) for row in range(test_df.shape[0]) for col in range(test_df.shape[1])]
for row, col in random.sample(ix, int(round(.1*len(ix)))):
    #test_df.iat[row, col] = np.nan
    test_df.iat[row, col] = None
test_df['A'] = test_df['A'].apply(str)
test_df['B'] = test_df['B'].apply(str)
test_df['C'] = test_df['C'].apply(str)
test_df['D'] = test_df['D'].apply(str)

print(type(test_df['A'].iloc[0]))

pd.to_numeric(test_df['A'], errors='coerce')
