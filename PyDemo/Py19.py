import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# s = pd.Series([1,3,5,np.nan,6,8])
# print(s)

dates = pd.date_range('20130101', periods=6)
# print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# print(df)

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
# print(df2)

# print(df.head(2))
# print(df.tail(2))

# print(df.index)
# print(df.columns)
# print(df.values)

# print(df.describe())

# print(df.T)

# print(df.sort_index(axis=1, ascending=False))

# print(df.sort_values(by='B'))

# print(df["A"])
# print(df[0:3])

# print(df["2013-01-01":"2013-01-03"])

# print(df.loc[dates[0]])
# print(df.loc[:,['A','B']])

# print(df.loc['20130102':'20130104',['A','B']])

# print(df.loc['20130102',['A','B']])

# print(df.loc[dates[0],'A'])

# print(df.at[dates[0],'A'])

# print(df.iloc[3])

# print(df.iloc[3:5,0:2])

# print(df.iloc[[1,2,4],[0,2]])

# print(df.iloc[:,1:3])

# print(df.iloc[1:3,:])

# print(df.iat[1,1])

# print(df[df.A > 0])

# print(df[df > 0])

# print(df2[df2['E'].isin(['two','four'])])

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
# print(df1)

# print(df1.dropna(how='any'))

# print(df1.fillna(value=5))

# print(pd.isnull(df1))

# print(df.apply(np.cumsum))

# print(df.apply(lambda x: x.max() - x.min()))

# s = pd.Series(np.random.randint(0, 7, size=10))
# print(s)

# print(s.value_counts())

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())


