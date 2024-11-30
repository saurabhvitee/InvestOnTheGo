from pyetfdb_scraper import etf
from pyetfdb_scraper.etf import ETF,load_etfs 
import mysql.connector as MSQC

def get_child(obj, path, default=None):
    try:
        child = obj[path[0]]
        for i in range(1, len(path)):
            child = child[path[i]]
        return child
    except:
        return default

def populate_etfdata(symbol, order):
    try:
        connection = MSQC.connect(
            host='localhost', database='etfdatabase', user='root', password='Kanishka@8510070031')
        cursor = connection.cursor(buffered=True)

        try:
                q="insert into etfdata values(%s,%s)"
                val=str(symbol,order)
                cursor.execute(q,val)
        except (connection.Error, connection.Warning):
            return {"message": "values not inserted"}
        
    except MSQC.Error as error:
        print("Failed to connect to database: {}".format(error))
    finally:
        connection.commit() 

def produce_performance_dict(symbol):
    symb = ETF(str(symbol))
    d = symb.performance['data']
    dict_ = {}
    for item in d:
        list = {}
        for i,j in item.items():
            if i=="":
                list['idx']=j
            else:
                list[i]=j
        return_ = list["idx"]
        sym_val=list[str(symbol)]
        dict_[return_]=sym_val
    return(dict_)


def populate_performance(symbol):
    d = produce_performance_dict(symbol)
    one_month = get_child(d, ['1 Month Return'])
    three_month = get_child(d, ['3 Month Return'])
    ytd_return = get_child(d, ['YTD Return'])
    one_year = get_child(d, ['1 Year Return'])
    three_year = get_child(d, ['3 Year Return'])
    five_year = get_child(d, ['5 Year Return'])
    try:
        connection = MSQC.connect(
            host='localhost', database='etfdatabase', user='root', password='Kanishka@8510070031')
        cursor = connection.cursor(buffered=True)

        try:
            q="insert into performance values(%s,%s,%s.%s,%s,%s,%s)"
            val=(symbol,one_month,three_month,ytd_return,one_year,three_year,five_year)
            cursor.execute(q,val)
        except (connection.Error, connection.Warning):
            return {"message": "values not inserted"}
        
    except MSQC.Error as error:
        print("Failed to connect to database: {}".format(error))
    finally:
        connection.commit() 

def populate_rankings(symbol):
    symb = ETF(str(symbol))
    d = symb.realtime_rankings
    Liquidity = get_child(d, ['data',0,'Metric Realtime Rating'])
    Expenses = get_child(d, ['data',1,'Metric Realtime Rating'])
    Performance = get_child(d, ['data',2,'Metric Realtime Rating'])
    Volatility = get_child(d, ['data',3,'Metric Realtime Rating'])
    Dividend = get_child(d, ['data',4,'Metric Realtime Rating'])
    Concentration = get_child(d, ['data',5,'Metric Realtime Rating'])
    try:
        connection = MSQC.connect(
            host='localhost', database='etfdatabase', user='root', password='Kanishka@8510070031')
        cursor = connection.cursor(buffered=True)

        try:
                q="insert into ratings values(%s,%s,%s,%s,%s,%s,%s)"
                val=(symbol,Liquidity,Expenses,Performance,Volatility,Dividend,Concentration)
                cursor.execute(q,val)
        except (connection.Error, connection.Warning):
            return {"message": "values not inserted"}
        
    except MSQC.Error as error:
        print("Failed to connect to database: {}".format(error))
    finally:
        connection.commit() 

def populate_technicals(symbol):
    symb = ETF(str(symbol))
    d = symb.technicals
    twenty_Day_MA = get_child(d, ['indicators','20 Day MA'])
    sixty_Day_MA = get_child(d, ['indicators','60 Day MA'])
    Average_Spread_dollar = get_child(d, ['indicators','Average Spread ($)'])
    Average_Spread_percentage = get_child(d, ['indicators','Average Spread (%)'])
    Lower_Bollinger_10_Day = get_child(d, ['indicators','Lower Bollinger (10 Day)'])
    Lower_Bollinger_20_Day = get_child(d, ['indicators','Lower Bollinger (20 Day)'])
    Lower_Bollinger_30_Day = get_child(d, ['indicators','Lower Bollinger (30 Day)'])
    MACD_100_Period = get_child(d, ['indicators','MACD 100 Period'])
    MACD_15_Period = get_child(d, ['indicators','MACD 15 Period'])
    Maximum_Premium_Discount = get_child(d, ['indicators','Maximum Premium Discount (%)'])
    Median_Premium_Discount = get_child(d, ['indicators','Median Premium Discount (%)'])
    RSI_10_Day = get_child(d, ['indicators','RSI 10 Day'])
    RSI_20_Day = get_child(d, ['indicators','RSI 20 Day'])
    RSI_30_Day = get_child(d, ['indicators','RSI 30 Day'])
    Resistance_Level_1 = get_child(d, ['indicators','Resistance Level 1'])
    Resistance_Level_2 = get_child(d, ['indicators','Resistance Level 2'])
    Stochastic_Oscillator_D_1Day = get_child(d, ['indicators','Stochastic Oscillator %D (1 Day)'])
    Stochastic_Oscillator_D_5Day = get_child(d, ['indicators','Stochastic Oscillator %D (5 Day)'])
    Stochastic_Oscillator_K_1Day = get_child(d, ['indicators','Stochastic Oscillator %K (1 Day)'])
    Stochastic_Oscillator_K_5Day = get_child(d, ['indicators','Stochastic Oscillator %K (5 Day)'])
    Support_Level_1 = get_child(d, ['indicators','Support Level 1'])
    Support_Level_2 = get_child(d, ['indicators','Support Level 2'])
    Tracking_Difference_Max_Downside = get_child(d, ['indicators','Tracking Difference Max Downside (%)'])
    Tracking_Difference_Max_Upside = get_child(d, ['indicators','Tracking Difference Max Upside (%)'])
    Tracking_Difference_Median = get_child(d, ['indicators','Tracking Difference Median (%)'])
    Ultimate_Oscillator = get_child(d, ['indicators','Ultimate Oscillator'])
    Upper_Bollinger_10Day = get_child(d, ['indicators','Upper Bollinger (10 Day)'])
    Upper_Bollinger_20Day = get_child(d, ['indicators','Upper Bollinger (20 Day)'])
    Upper_Bollinger_30Day = get_child(d, ['indicators','Upper Bollinger (30 Day)'])
    Williams_Range_10Day = get_child(d, ['indicators','Williams % Range 10 Day'])
    Williams_Range_20Day = get_child(d, ['indicators','Williams % Range 20 Day'])
    five_day_volatility = get_child(d, ['volatility','data', '5 Day Volatility', 0])
    twenty_day_volatility = get_child(d, ['volatility','data', '20 Day Volatility', 0])
    fifty_day_volatility = get_child(d, ['volatility','data', '50 Day Volatility', 0])
    twohund_day_volatility = get_child(d, ['volatility','data', '200 Day Volatility', 0])
    beta = get_child(d, ['volatility','data', 'Beta', 0])
    standard_deviation = get_child(d, ['volatility','data', 'Standard Deviation', 0])
    try:
        connection = MSQC.connect(
            host='localhost', database='etfdatabase', user='root', password='Kanishka@8510070031')
        cursor = connection.cursor(buffered=True)

        try:
        
                q="insert into technicals values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
                val=(symbol,twenty_Day_MA,sixty_Day_MA,Average_Spread_dollar,Average_Spread_percentage,
                Lower_Bollinger_10_Day,Lower_Bollinger_20_Day,Lower_Bollinger_30_Day,MACD_100_Period,MACD_15_Period,
                Maximum_Premium_Discount,Median_Premium_Discount,RSI_10_Day,RSI_20_Day,
                RSI_30_Day,Resistance_Level_1,Resistance_Level_2,Stochastic_Oscillator_D_1Day,
                Stochastic_Oscillator_D_5Day,Stochastic_Oscillator_K_1Day,Stochastic_Oscillator_K_5Day,
                Support_Level_1,Support_Level_2,Tracking_Difference_Max_Downside,Tracking_Difference_Max_Upside,
                Tracking_Difference_Median,Ultimate_Oscillator,Upper_Bollinger_10Day,Upper_Bollinger_20Day,
                Upper_Bollinger_30Day,Williams_Range_10Day,Williams_Range_20Day,five_day_volatility,
                    twenty_day_volatility,fifty_day_volatility,twohund_day_volatility,beta,standard_deviation)
                cursor.execute(q,val)
        except (connection.Error, connection.Warning):
            return {"message": "values not inserted"}
        
    except MSQC.Error as error:
        print("Failed to connect to database: {}".format(error))
    finally:
        connection.commit() 

def calculate_price(symbol):
    try:
        connection = MSQC.connect(
            host='localhost', database='etfdatabase', user='root', password='Kanishka@8510070031')
        cursor = connection.cursor(buffered=True)
        cursor2 = connection.cursor(buffered=True)

        try:
                q1="select * from technicals where etfsymbol = %s"
                val1=(symbol)
                cursor.execute(q1,val1)
                q2="select * from technicals where etfsymbol = %s"
                val2=(symbol)
                cursor2.execute(q2,val2)
        except (connection.Error, connection.Warning):
            return {"message": "values not inserted"}
        
        try:
            res_lvl = cursor.fetchone()[15]
            supp_lvl = cursor2.fetchone()[21]
        except (connection.Error, connection.Warning):
            return {"message": "connection failed, login failed"}
        
        try:
            res_lvl = float(str(res_lvl[1:]))
            supp_lvl = float(str(supp_lvl[1:]))
            return((res_lvl + supp_lvl)/2)
        except:
            return None
        
        
    except MSQC.Error as error:
        print("Failed to connect to database: {}".format(error))
        return None
    finally:
        connection.commit() 

def populate_info(symbol):
    symb = ETF(str(symbol))
    d = symb.info
    fiftytwo_Week_Hi = get_child(d, ['trade_data','data','52 Week Hi'])
    fiftytwo_Week_Lo = get_child(d, ['trade_data','data','52 Week Lo'])
    AUM = get_child(d, ['trade_data','data','AUM'])
    Leveraged = get_child(d, ['dbtheme','data','Leveraged','text'], 1)
    Asset_Class = get_child(d, ['dbtheme','data','Asset Class','text'])
    Asset_Class_Size = get_child(d, ['dbtheme','data','Asset Class Size','text'])
    Asset_Class_Style = get_child(d, ['dbtheme','data','Asset Class Style','text'])
    Brand = get_child(d, ['vitals','data','Brand','text'])
    Category1 = get_child(d, ['fact_set','data','Category',0])
    Category2 = get_child(d, ['dbtheme','data','Category','text'])
    ETF_Home_Page = get_child(d, ['vitals','data','ETF Home Page','text'])
    Expense_Ratio = get_child(d, ['vitals','data','Expense Ratio','text'])
    Focus = get_child(d, ['fact_set','data','Focus',0])
    Inception = get_child(d, ['vitals','data','Inception','text'])
    Index_Tracked = get_child(d, ['vitals','data','Index Tracked','text'])
    Issuer = get_child(d, ['vitals','data','Issuer','text'])
    Niche = get_child(d, ['fact_set','data','Niche',0])
    Price = calculate_price(symbol)
    General_Region = get_child(d, ['dbtheme','data','Region (General)','text'])
    Specific_region = get_child(d, ['dbtheme','data','Region (Specific)','text'])
    General_Sector = get_child(d, ['dbtheme','data','Sector (General)','text'])
    Specific_Sector = get_child(d, ['dbtheme','data','Sector (Specific)','text'])
    Segment = get_child(d, ['fact_set','data','Segment',0])
    Shares = get_child(d, ['trade_data','data','Shares'])
    Strategy = get_child(d, ['fact_set','data','Strategy',0])
    Structure = get_child(d, ['vitals','data','Structure','text'])
    Weighting_Scheme = get_child(d, ['fact_set','data','Weighting Scheme',0])
    try:
        connection = MSQC.connect(
            host='localhost', database='etfdatabase', user='root', password='Kanishka@8510070031')
        cursor = connection.cursor(buffered=True)

        try:
                info_update="insert into info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(symbol ,fiftytwo_Week_Hi,fiftytwo_Week_Lo,AUM,Leveraged,Asset_Class,Asset_Class_Size,Asset_Class_Style,Brand,Category1,Category2,ETF_Home_Page,Expense_Ratio,Focus,Inception,
                               Index_Tracked,Issuer,Niche,Price,
                               General_Region,Specific_region,General_Sector,Specific_Sector,Segment,
                                Shares,Strategy,Structure,Weighting_Scheme)
                cursor.execute(info_update,val)
                connection.commit()
        except (connection.Error, connection.Warning):
            return {"message": "values not inserted"}
        
    except MSQC.Error as error:
        print("Failed to connect to database: {}".format(error))
    finally:
        connection.commit() 



etfs = load_etfs()[:500]

for i in range(len(etfs)):
    populate_etfdata(etfs[i], i+1)
    populate_rankings(etfs[i])
    populate_performance(etfs[i])
    populate_technicals(etfs[i])
    populate_info(etfs[i])
