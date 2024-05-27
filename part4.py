import pandas as pd
import matplotlib.pyplot as plt

data = {'value': [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}

df = pd.DataFrame(data)

# df.plot.hist() # Столбчатая диаграмма
df.boxplot(column='value')
plt.show()

Q1 = df.quantile(0.25) # Первый квартиль
Q3 = df.quantile(0.75) # Третий квартиль
IQR = Q3 - Q1 # Межквартильный размах


downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]
df_new.boxplot(column='value')
plt.show()