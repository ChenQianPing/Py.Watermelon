# import pymssql
import pandas as pd
from sqlalchemy import create_engine
import tushare as ts

# conn = pymssql.connect(host='47.96.141.232', user='sa', password='sh.123456', database='WatermelonDb')

# cur = conn.cursor()
# cur.execute('select top 5 * from [dbo].[Act_Action]')
# print(cur.fetchall())
# cur.close()

# 读取SqlServer数据
# df = pd.read_sql("select top 5 * from [dbo].[Act_Action]", con=conn)
# print(df)

# conn.close()

engine = create_engine('mssql+pymssql://sa:sh.123456@47.96.141.232/WatermelonDb', echo=True)

# 龙虎榜数据-个股上榜统计
# df1 = ts.cap_tops(5)
# df2 = ts.cap_tops(10)
# df3 = ts.cap_tops(30) #HTTP Error 500: Internal Server Error

# df4 = ts.get_industry_classified() # 行业分类
# df5 = ts.get_concept_classified() # 概念分类
# df6 = ts.get_area_classified() # 地域分类
# df7 = ts.get_sme_classified()  # 中小板分类
# df8 = ts.get_gem_classified() # 创业板分类
# df9 = ts.get_st_classified() # 风险警示板分类

# df10 = ts.get_hs300s() # 沪深300成份及权重
# df11 = ts.get_sz50s() # 上证50成份股
# df12 = ts.get_zz500s() # 中证500成份股
# df13 = ts.get_terminated() # 终止上市股票列表，取不到数据
# df14 = ts.get_suspended() # 暂停上市股票列表，取不到数据

df15 = ts.get_stock_basics()

print(df15)
print("Start Sync")

# 存入数据库
# df1.to_sql('Tus_CapTops5', engine, if_exists='replace')
# df2.to_sql('Tus_CapTops10', engine, if_exists='replace')
# df3.to_sql('Tus_CapTops30', engine, if_exists='replace')

# df4.to_sql('Tus_IndustryClassified', engine, if_exists='replace')
# df5.to_sql('Tus_ConceptClassified', engine, if_exists='replace')
# df6.to_sql('Tus_AreaClassified', engine, if_exists='replace')
# df7.to_sql('Tus_SmeClassified', engine, if_exists='replace')
# df8.to_sql('Tus_GemClassified', engine, if_exists='replace')
# df9.to_sql('Tus_StClassified', engine, if_exists='replace')

# df10.to_sql('Tus_Hs300s', engine, if_exists='replace')
# df11.to_sql('Tus_Sz50s', engine, if_exists='replace')
# df12.to_sql('Tus_Zz500s', engine, if_exists='replace')
# df13.to_sql('Tus_Terminated', engine, if_exists='replace')

df15.to_sql('Tus_StockBasics', engine, if_exists='replace', index=False)
# df15.to_csv('F:/01/Tus_StockBasics.csv', encoding='utf_8_sig')

print("Synchronous Data Successful")







