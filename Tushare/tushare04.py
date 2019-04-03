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
# df3 = ts.cap_tops(30)


# 存入数据库
# df1.to_sql('Tus_CapTops5', engine, if_exists='replace')
# df2.to_sql('Tus_CapTops10', engine)
# df3.to_sql('Tus_CapTops30', engine)


# df4 = ts.get_industry_classified() # 行业分类
# df5 = ts.get_concept_classified() # 概念分类
# df6 = ts.get_area_classified() # 地域分类
# df7 = ts.get_sme_classified()  # 中小板分类
# df8 = ts.get_gem_classified() # 创业板分类
# df9 = ts.get_st_classified() # 风险警示板分类
df10 = ts.get_sz50s()
print(df10)

print("Start Sync")

# df4.to_sql('Tus_IndustryClassified', engine, if_exists='replace')
# df5.to_sql('Tus_ConceptClassified', engine, if_exists='replace')
# df6.to_sql('Tus_AreaClassified', engine, if_exists='replace')
# df7.to_sql('Tus_SmeClassified', engine, if_exists='replace')
# df8.to_sql('Tus_GemClassified', engine, if_exists='replace')
# df9.to_sql('Tus_StClassified', engine, if_exists='replace')
# df10.to_sql('Tus_Hs300s', engine, if_exists='replace')

print("Synchronous Data Successful")







