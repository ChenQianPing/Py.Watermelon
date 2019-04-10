# 本代码由可视化策略环境自动生成 2019年4月10日 12:10
# 本代码单元只能在可视化模式下编辑。您也可以拷贝代码，粘贴到新建的代码单元或者策略，然后修改。


# 回测引擎：每日数据处理函数，每天执行一次
def m19_handle_data_bigquant_run(context, data):
    # 按日期过滤得到今日的预测数据
    ranker_prediction = context.ranker_prediction[
        context.ranker_prediction.date == data.current_dt.strftime('%Y-%m-%d')]

    # 1. 资金分配
    # 平均持仓时间是hold_days，每日都将买入股票，每日预期使用 1/hold_days 的资金
    # 实际操作中，会存在一定的买入误差，所以在前hold_days天，等量使用资金；之后，尽量使用剩余资金（这里设置最多用等量的1.5倍）
    is_staging = context.trading_day_index < context.options['hold_days'] # 是否在建仓期间（前 hold_days 天）
    cash_avg = context.portfolio.portfolio_value / context.options['hold_days']
    cash_for_buy = min(context.portfolio.cash, (1 if is_staging else 1.5) * cash_avg)
    cash_for_sell = cash_avg - (context.portfolio.cash - cash_for_buy)
    positions = {e.symbol: p.amount * p.last_sale_price
                 for e, p in context.perf_tracker.position_tracker.positions.items()}

    # 2. 生成卖出订单：hold_days天之后才开始卖出；对持仓的股票，按机器学习算法预测的排序末位淘汰
    if not is_staging and cash_for_sell > 0:
        equities = {e.symbol: e for e, p in context.perf_tracker.position_tracker.positions.items()}
        instruments = list(reversed(list(ranker_prediction.instrument[ranker_prediction.instrument.apply(
                lambda x: x in equities and not context.has_unfinished_sell_order(equities[x]))])))
        # print('rank order for sell %s' % instruments)
        for instrument in instruments:
            context.order_target(context.symbol(instrument), 0)
            cash_for_sell -= positions[instrument]
            if cash_for_sell <= 0:
                break

    # 3. 生成买入订单：按机器学习算法预测的排序，买入前面的stock_count只股票
    buy_cash_weights = context.stock_weights
    buy_instruments = list(ranker_prediction.instrument[:len(buy_cash_weights)])
    max_cash_per_instrument = context.portfolio.portfolio_value * context.max_cash_per_instrument
    for i, instrument in enumerate(buy_instruments):
        cash = cash_for_buy * buy_cash_weights[i]
        if cash > max_cash_per_instrument - positions.get(instrument, 0):
            # 确保股票持仓量不会超过每次股票最大的占用资金量
            cash = max_cash_per_instrument - positions.get(instrument, 0)
        if cash > 0:
            context.order_value(context.symbol(instrument), cash)

# 回测引擎：准备数据，只执行一次
def m19_prepare_bigquant_run(context):
    pass

# 回测引擎：初始化函数，只执行一次
def m19_initialize_bigquant_run(context):
    # 加载预测数据
    context.ranker_prediction = context.options['data'].read_df()

    # 系统已经设置了默认的交易手续费和滑点，要修改手续费可使用如下函数
    context.set_commission(PerOrder(buy_cost=0.0003, sell_cost=0.0013, min_cost=5))
    # 预测数据，通过options传入进来，使用 read_df 函数，加载到内存 (DataFrame)
    # 设置买入的股票数量，这里买入预测股票列表排名靠前的2只
    stock_count = 2
    # 每只的股票的权重，如下的权重分配会使得靠前的股票分配多一点的资金，[0.339160, 0.213986, 0.169580, ..]
    context.stock_weights = T.norm([1 / math.log(i + 2) for i in range(0, stock_count)])
    # 设置每只股票占用的最大资金比例
    context.max_cash_per_instrument = 0.2
    context.options['hold_days'] = 1


# m1 确定数据：训练集

# 证券代码列表
# 定义:M.instruments.v2(start_date,end_date,market='CN_STOCK_A',instrument_list='',max_count=0)
# 参数:
# start_date (字符串) – 开始时间
# end_date (字符串) – 结束时间
# market – 证券市场，默认值是 CN_STOCK_A (中国A股)，更多见 交易市场
# instrument_list：可选，代码，默认值null，股票代码列表，每行一个，如果指定，market参数将被忽略
# max_count：可选，整数，默认值0，最大值2147483647，最小值-2147483648，最大数量，0表示没有限制，一般用于在小数据上测试和调试问题

# 返回类型:
# Outputs - (dict), 一个含有时间以及股票列表的字典 data：data，证券数据

m1 = M.instruments.v2(
    start_date='2019-01-01',
    end_date='2019-04-01',
    market='CN_STOCK_A',
    instrument_list='',
    max_count=0
)


# m2 自动标注-股票
#
# 高级数据标注
# 定义
# M.advanced_auto_labeler.v2(instruments, label_expr,
# start_date, end_date, benchmark, drop_na_label, cast_label_int, user_functions)

# advanced_auto_labeler可以使用表达式，对数据做任何标注。比如基于未来给定天数的收益/波动率等数据，来实现对数据做自动标注。

# 参数:
#
# instruments(列表|DataSource) — 证券代码列表，默认由M.instruments模块传入
# labelexpr (列表) – 标注表达式，可以使用多个表达式，顺序执行，从第二个开始，可以使用label字段。可用数据字段见 历史数据，添加benchmark前缀，可使用对应的benchmark数据。可用操作符和函数见 表达式引擎
# start_date(str) — 起始时间，默认为空值，由M.instruments模块传入
# end_date(str) — 结束时间，默认为空值，由M.instruments模块传入
# benchmark(str) — 指定的benchmark前缀表达式对应的标注基准，默认为’000300.SHA’
# drop_na_label (bool) – 删除无标注数据，是否删除没有标注的数据；默认值是True。
# cast_label_int (bool) – 将标注转换为整数，一般用于分类学习；默认值是True。
# user_functions—(字典) – 自定义表达式函数，字典格式，例:{‘user_rank’:user_rank}，字典的key是方法名称，字符串类型，字典的value是方法的引用，参考表达式引擎；默认值是{}
# 返回:
#
# 标注数据


m2 = M.advanced_auto_labeler.v2(
    instruments=m1.data,
    label_expr="""# #号开始的表示注释
# 0. 每行一个，顺序执行，从第二个开始，可以使用label字段
# 1. 可用数据字段见 https://ppe.bigquant.com/docs/data_history_data.html
#   添加benchmark_前缀，可使用对应的benchmark数据
# 2. 可用操作符和函数见 `表达式引擎 <https://ppe.bigquant.com/docs/big_expr.html>`_

# 计算收益：5日收盘价(作为卖出价格)除以明日开盘价(作为买入价格)
shift(close, -5) / shift(open, -1)

# 极值处理：用1%和99%分位的值做clip
clip(label, all_quantile(label, 0.01), all_quantile(label, 0.99))

# 将分数映射到分类，这里使用20个分类
all_wbins(label, 20)

# 过滤掉一字涨停的情况 (设置label为NaN，在后续处理和训练中会忽略NaN的label)
where(shift(high, -1) == shift(low, -1), NaN, label)
""",
    start_date='',
    end_date='',
    benchmark='000300.SHA',
    drop_na_label=True,
    cast_label_int=True
)

# m3 输入特征列表

# 输入特征列表
# 定义 M.input_features.v1(features)
# 示例代码
# M.input_features.v1(features=['shift(close_0+open_1)']).data.read()

# return_5 5日收益
# return_10 10日收益
# return_20 20日收益
# avg_amount_0/avg_amount_5 当日/5日平均交易额
# avg_amount_5/avg_amount_20 5日/20日平均交易额
# rank_avg_amount_0/rank_avg_amount_5  # 当日/5日平均交易额排名
# rank_avg_amount_5/rank_avg_amount_10 # 5日/10日平均交易额排名
# rank_return_0  # 当日收益排名
# rank_return_5  # 5日收益排名
# rank_return_10 # 10日收益排名
# rank_return_0/rank_return_5 # 当日/5日平均收益排名
# rank_return_5/rank_return_10 # 5日/10日平均收益排名
# pe_ttm_0 市盈率 (TTM)

# 'close_5/close_0',  # 5日收益
# 'close_10/close_0',  # 10日收益
# 'close_20/close_0',  # 20日收益

m3 = M.input_features.v1(
    features="""# #号开始的表示注释
# 多个特征，每行一个，可以包含基础特征和衍生特征
return_5
return_10
return_20
avg_amount_0/avg_amount_5
avg_amount_5/avg_amount_20
rank_avg_amount_0/rank_avg_amount_5
rank_avg_amount_5/rank_avg_amount_10
rank_return_0
rank_return_5
rank_return_10
rank_return_0/rank_return_5
rank_return_5/rank_return_10
pe_ttm_0
"""
)


# m15 基础特征抽取
# 基础特征(因子）抽取
# 定义
# M.general_feature_extractor.v7(self, instruments, features, start_date='', end_date='', before_start_days=0)
# 基础特征(因子)抽取：读取基础数据字段，这里抽取的是基础特征，例如，对于特征 close_1/close_0，这里会读取出 close_0，close_1

# 参数：
#
# instruments (列表|DataSource) – 证券代码列表。训练集
# features (列表|DataSource) – 特征列表。
# start_date (str) – 开始日期，示例 2017-02-12，一般不需要指定，使用 证券代码列表 里的开始日期；默认值是空。
# end_date (str) – 结束日期，示例 2017-02-12，一般不需要指定，使用 证券代码列表 里的结束日期；默认值是空。
# before_start_days (int) – 向前取数据天数，比如，用户通过表达式计算的衍生特征，可能需要用到开始日期之前的数据，
# 可以通过设置此值实现，则数据将从 开始日期-向前取数据天数 开始取。考虑到节假日等，建议将此值得大一些；默认值是0。


m15 = M.general_feature_extractor.v7(
    instruments=m1.data,
    features=m3.data,
    start_date='',
    end_date='',
    before_start_days=0
)

# m16 衍生特征抽取
# 衍生特征抽取
# 定义 M.derived_feature_extractor.v2(self, input_data, features, date_col='date',
# instrument_col='instrument', user_functions={})

# 衍生特征(因子)抽取：对于衍生特征（通过表达式定义的，e.g. close_1/close_0），通过表达式引擎，计算表其值

# 参数:
#
# input_data (DataSource) – 特征数据，包含用于构建衍生因子的基础因子数据，一般来自基础特征抽取或者衍生特征抽取模块。
# features (列表|DataSource) – 特征列表，需要抽取的衍生特征，由表达式构建。可用数据字段来自输入的data，可用操作符和函数见表达式引擎 。
# date_col (str) – 日期列名，如果在表达式中用到切面相关函数时，比如 rank，会用到此列名；默认值是date。
# instrument_col (str) – 证券代码列名，如果在表达式中用到时间序列相关函数时，比如 shift，会用到此列名；默认值是instrument。
# user_functions (字典) – 自定义表达式函数，字典格式，例:{‘user_rank’:user_rank}，字典的key是方法名称，字符串类型，字典的value是方法的引用，参考表达式引擎 ；默认值是{}。
# drop_na：必选，布尔，默认值False，删除na数据，删除存在空数据(NA)的行
# remove_extra_columns：必选，布尔，默认值False，删除多余的列，删除不在输入特征、日期和证券代码的列

m16 = M.derived_feature_extractor.v3(
    input_data=m15.data,
    features=m3.data,
    date_col='date',
    instrument_col='instrument',
    drop_na=False,
    remove_extra_columns=False
)

# m7 连接数据
# 连接数据
# 定义 M.join.v3(data1, data2, on='date, instrument', how='inner', sort=False)
# 连接两个DataSource (数据内容DataFrame)

# 参数:
#
# data1 (DataSource) – 第一个输入数据。m2 自动标注-股票
# data2 (DataSource) – 第二个输入数据。 m16 衍生特征抽取
# on (str) – 关联列，多个列用英文逗号分隔；默认值是date,instrument。
# how (choice) – 连接方式；可选值有: left, right, outer, inner；默认值是inner。
# sort (bool) – 对结果排序；默认值是False。

m7 = M.join.v3(
    data1=m2.data,
    data2=m16.data,
    on='date,instrument',
    how='inner',
    sort=False
)


# m13 缺失数据处理
m13 = M.dropnan.v1(
    input_data=m7.data
)


# m9 预测数据,用于回测和模拟
m9 = M.instruments.v2(
    start_date=T.live_run_param('trading_date', '2019-01-01'),
    end_date=T.live_run_param('trading_date', '2019-04-01'),
    market='CN_STOCK_A',
    instrument_list='',
    max_count=0
)

# m17 基础特征抽取
m17 = M.general_feature_extractor.v7(
    instruments=m9.data,
    features=m3.data,
    start_date='',
    end_date='',
    before_start_days=0
)

# m18 衍生特征抽取
m18 = M.derived_feature_extractor.v3(
    input_data=m17.data,
    features=m3.data,
    date_col='date',
    instrument_col='instrument',
    drop_na=False,
    remove_extra_columns=False
)

# m14 缺失数据处理
m14 = M.dropnan.v1(
    input_data=m18.data
)

# m4 StandardScaler标准化
m4 = M.preprocessing_standard_scaler.v1(
    training_ds=m13.data,
    features=m3.data,
    predict_ds=m14.data,
    with_mean=True,
    with_std=True
)

# m6 StockRanker训练
# StockRanker训练
# M.stock_ranker_train.v5(self, training_ds, features, test_ds=None, learning_algorithm='排序',
# number_of_leaves=30,minimum_docs_per_leaf=1000, number_of_trees=20, learning_rate=0.1,max_bins=1023,
# feature_fraction=1, base_model=None,rolling_input=None)
# StockRanker排序学习模型训练。StockRanker属于集成学习，模型由多棵决策树组成，所有树的结论累加起来做为最终决策分数。

# 参数:
#
# training_ds (DataSource) – 训练数据，需要包含所有用到的特征数据，包括基础特征和衍生特征。
# features (列表|DataSource) – 特征列表。
# test_ds (DataSource) – 测试数据集，可用于在训练阶段查看训练效果，来做模型参数和特征等的调优；通过配置early stop参数可以让训练提前终止；默认值是None。
# learning_algorithm (choice) – 学习算法，机器学习优化算法；可选值有: 排序, 回归, 二分类, logloss；默认值是排序。
# number_of_leaves (int) – 叶节点数量：每棵树最大叶节点数量。一般情况下，叶子节点越多，则模型越复杂，表达能力越强，过拟合的可能性也越高；默认值是30。
# minimum_docs_per_leaf (int) – 每叶节点最小样本数：每个叶节点最少需要的样本数量，一般值越大，泛化性性越好；默认值是1000。
# number_of_trees (int) – 树的数量：一般情况下，树越多，则模型越复杂，表达能力越强，过拟合的可能性也越高；默认值是20。
# learning_rate (float) – 学习率：学习率如果太大，可能会使结果越过最优值，如果太小学习会很慢；默认值是0.1。
# max_bins (int) – 特征值离散化数量：一般情况下，max_bins越大，则学的越细，过拟合的可能性也越高；默认值是1023。
# feature_fraction (int) – 特征使用率：在构建每一颗树时，每个特征被使用的概率，如果为1，则每棵树都会使用所有特征；默认值是1。
# base_model (字符串) – 基础模型，可以在此模型上继续训练；默认值是None。
# rolling_input (dict) – 滚动运行参数，接收来自滚动运行的输入，用于训练数据过滤；默认值是None。
# feature_fraction：可选，浮点数，默认值1，最大值1，最小值0，特征使用率：在构建每一颗树时，每个特征被使用的概率，如果为1，
# 则每棵树都会使用所有特征
# m_lazy_run：必选，布尔，默认值False，延迟运行，在延迟运行模式下，模块不会直接运行，将被打包，
# 通过端口 延迟运行 输出，可以作为其他模块的输入，并在其他模块里开启运行

# 返回:
#
# .model: 模型
# .feature_gains: 特征贡献
# .m_lazy_run: 延迟运行，将当前模块打包，可以作为其他模块的输入，在其他模块里运行。启用需要勾选模块的 延迟运行 参数。

m6 = M.stock_ranker_train.v5(
    training_ds=m4.transform_trainds,
    features=m3.data,
    learning_algorithm='排序',
    number_of_leaves=30,
    minimum_docs_per_leaf=1000,
    number_of_trees=20,
    learning_rate=0.1,
    max_bins=1023,
    feature_fraction=1,
    m_lazy_run=False
)

# m8 StockRanker预测
# StockRanker预测
# 定义#
# M.stock_ranker_predict.v5(self, model, data)
# 股票排序机器学习模型预测。支持来自滚动运行输出的多个模型。
#
# 参数:#
# model (字符串) – 模型。
# data (DataSource) – 数据。
# 返回：
#
# .predictions: 预测结果
# .m_lazy_run: 延迟运行，将当前模块打包，可以作为其他模块的输入，在其他模块里运行。启用需要勾选模块的 延迟运行 参数。

m8 = M.stock_ranker_predict.v5(
    model=m6.model,
    data=m4.transform_predictds,
    m_lazy_run=False
)


# m19 Trade（回测/模拟）
# Trade (回测/模拟) (v4)

# 量化交易引擎主入口。
#
# 参数:#
# start_date (str) – 开始日期，设定值只在回测模式有效，在模拟实盘模式下为当前日期。一般不需要指定，使用证券代码列表里的开始日期
# end_date (str) – 结束日期，设定值只在回测模式有效，在模拟实盘模式下为当前日期。一般不需要指定，
# 使用证券代码列表里的结束日期
# handle_data (function) – [回调函数]主函数，必须实现的函数，
# 该函数每个单位时间(每根K线)会调用一次,
# 如果按天回测,则每天调用一次,
# 如果按分钟,则每分钟调用一次。在回测中，可以通过对象data获取单只股票或多只股票的时间窗口价格数据。如果算法中没有schedule_function函数，那么该函数为必选函数。一般策略的交易逻辑和订单生成体现在该函数中；默认值是None
#
# instruments (list|DataSource) – 证券代码列表，如果提供了 prepare 函数，可以在 prepare 中覆盖此参数提供的值；默认值是None
# options_data (DataSource) – 其他输入数据：回测中用到的其他数据，比如预测数据、训练模型等。如果设定，在回测中通过 context.options['data']调用；默认值是None
# history_ds (DataSource) – 回测有价格撮合过程，需要传入标的价格数据
# benchmark (DataSource) – 基准数据，不影响回测结果，需要传入自定义的数据作为策略比较基准。暂时不支持参数为字符串(str)，需要传入用户自定义的DataSource
# trading_calendar - 交易日历。默认情况下，为中国A股市场的交易日历，如果是分钟回测或其他市场回测，需要自定义交易日历
# prepare (function) – [回调函数]数据准备函数，运行过程中只调用一次，在initialize前调用，准备交易中需要用到数据；默认值是None
# initialize (function) – [回调函数]初始化函数，整个回测中只在最开始时调用一次，
# 用于初始化一些账户状态信息和策略基本参数，context也可以理解为一个全局变量，在回测中存放当前账户信息和策略基本参数便于会话；默认值是None
# before_trading_start (function) – [回调函数]盘前处理函数，每日开盘前调用一次。该函数是可选函数，
# 在handle_data函数之前运行。你的算法可以在该函数中进行一些数据处理计算，比如确定当天有交易信号的股票池；默认值是None
# volume_limit (float) – 成交率限制：执行下单时控制成交量参数，若设置为０时，不进行成交量检查；默认值是0.025，
# 下单量如果超过该K线成交量的0.025，多余的订单量会自动取消
# order_price_field_buy (str) – 买入点：open=开盘买入，close=收盘买入；可选值有: 'open'，'close'；默认值是'open'
# order_price_field_sell (str) – 卖出点：open=开盘卖出，close=收盘卖出；可选值有: 'open'，'close'；默认值是'close'
# capital_base (float) – 初始资金；默认值是1000000.0
# product_type(str) - 交易品种类型，默认为product_type='股票'，如果是期货，需要指定product_type='期货'，这里股票用stock、期货用future同理
# auto_cancel_non_tradable_orders (bool) – 自动取消无法成交的订单。是否自动取消因为停牌、一字涨跌停等原因不能成交的订单；默认值是True
# data_frequency (str) – 回测数据频率，可选值有: 'daily'和'minute'；默认值是daily
# price_type (str) – 回测价格类型：前复权(forward_adjusted)，真实价格(original)，后复权(backward_adjusted)；
# 可选值有: 前复权, 真实价格, 后复权；默认值是后复权。
# plot_charts (bool) – 显示回测结果图表；默认值是True
# backtest_only (bool) – 只在回测模式下运行：默认情况下，Trade会在回测和实盘模拟模式下都运行。如果策略中有多个M.trade，
# 在实盘模拟模式下，只能有一个设置为运行，其他的需要设置为 backtest_only=True，否则将会有未定义的行为错误；默认值是False
# options (dict) – 用户自定义数据，在回调函数中要用到的外部数据（例如生成交易信号的数据），可以从这里传入，并通过 context.options进行调用；默认值是None
# m_deps(float|str) - 模块依赖项，M开头是模块(Module)的通用标识。为了节省运行时间，采取了缓存机制，每次运行会检查各个模块的参数是否有修改，如果没有修改，就启用缓存数据，如果有修改就重新运行。
# 如果我们不想击中缓存，每次想重新运行的话就可以修改M.trade模块的各个参数项，最简单的方法就是设置m_deps=np.random.randn()，这样就能保证主函数、初始化函数等函数内部修改以后按最新的代码运行结果。
#
# 返回：
# .raw_perf: 回测详细数据
#
# 返回类型:
# Outputs -回测结果数据
#
# 股票
# date - timestamp|datetime 必选 日期
# instrument - str 必选 股票代码
# open - float 必选 开盘价
# high - float 必选 最高价
# low - float 必选 最低价
# close - float 必选 收盘价
# volume - float 必选 成交量
# adjust_factor - float 必选 复权因子。对于股票回测而言，需要知道价格及复权因子
# price_limit_status - float 可选 股价在收盘时的涨跌停状态：1表示跌停，2表示未涨跌停，3则表示涨停
# 回测数据如果是股票，复权因子是需要的，价格涨跌停状态是可选的，因为可以通过价格涨跌停状态数据来进行订单管理，比如涨停并且是收盘买入，那么该笔订单无法成交。

m19 = M.trade.v4(
    instruments=m9.data,
    options_data=m8.predictions,
    start_date='',
    end_date='',
    handle_data=m19_handle_data_bigquant_run,
    prepare=m19_prepare_bigquant_run,
    initialize=m19_initialize_bigquant_run,
    volume_limit=0.025,
    order_price_field_buy='open',  # 开盘买入
    order_price_field_sell='close',  # 收盘卖出
    capital_base=1000000,  # 初始资金
    auto_cancel_non_tradable_orders=True,
    data_frequency='daily',
    price_type='后复权',
    product_type='股票',
    plot_charts=True,
    backtest_only=False,
    benchmark='000300.SHA'
)