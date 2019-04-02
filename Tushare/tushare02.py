import tushare as ts


# df = ts.get_stock_basics()
# df.to_csv('F:/01/get_stock_basics.csv')
# df.to_csv('F:/01/get_stock_basics.csv', encoding='utf_8_sig')


# 沪深股票列表
#
# ts.get_stock_basics()
#
# code,代码  name,名称  industry,所属行业   area,地区   pe,市盈率   outstanding,流通股本(亿)   totals,总股本(亿)   totalAssets,总资产(万)   liquidAssets,流动资产
#
# fixedAssets,固定资产   reserved,公积金   reservedPerShare,每股公积金   esp,每股收益   bvps,每股净资   pb,市净率   timeToMarket,上市日期
#
# undp,未分利润   perundp, 每股未分配   rev,收入同比(%)   profit,利润同比(%)   gpr,毛利率(%)   npr,净利润率(%)   holders,股东人数

# df = ts.get_report_data(2018,3)
# df.to_csv('F:/01/get_report_data.csv', encoding='utf_8_sig')

# 行业分类
# df = ts.get_industry_classified()
# df.to_csv('F:/01/get_industry_classified.csv', encoding='utf_8_sig')

# 2.概念分类
# df = ts.get_concept_classified()
# df.to_csv('F:/01/get_concept_classified.csv', encoding='utf_8_sig')

# 1.存款利率
# print(ts.get_deposit_rate())

# 2.贷款利率
# print(ts.get_loan_rate())


# print(ts.top_list('2019-04-02'))

df = ts.cap_tops(10) # 默认为5日

df.to_csv('F:/01/cap_tops.csv', encoding='utf_8_sig')
# df.to_json('F:/01/cap_tops.json')









