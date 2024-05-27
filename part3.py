import pandas as pd
import numpy as np

dates = pd.date_range(start='2022-07-26', periods=10, freq='D')

values = np.random.rand(10)

df = pd.DataFrame({'Data': dates, 'Value': values})
print(df)

df.set_index('Data', inplace=True)

month = df.resample('М').mean()
print(month)

