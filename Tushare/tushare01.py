import tushare as ts
from pandas import DataFrame

# print(tushare.__version__)

# 获取股票新闻
data = ts.get_notices(code="002131")  # 返回的对象是一个<class 'pandas.core.frame.DataFrame'>
# 使用pandas处理返回的对象
frame1 = DataFrame(data, columns=["title"],index=[0, 1, 2])  # 只获取标题和url,并且只获取最近的3条记录
# print(frame1)


# 获取股票的历史行情
# 上证指数 深圳成指 沪深300指数 上证50 中小板 创业板
# 'sh','sz','hs300','sz50','zxb','cyb'
hist = ts.get_hist_data('sh',start='2019-03-25',end='2019-04-02')

# 只获取股票的开盘价和收盘价
# frame2 = DataFrame(hist, columns=["open", "close", "low", "high", "volume", "p_change", "price_change", "ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"])
# print(frame2)


# frame2.to_csv('F:/01/sh.csv')

# df = ts.get_index()
# print(df)

df = ts.get_index()
df.to_csv('F:/01/get_index.csv')
print(df)

