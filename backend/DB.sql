create database if not exists cash_by_chance;
use cash_by_chance;

DROP TABLE IF EXISTS login_details;
CREATE TABLE login_details (
  username varchar(128) NOT NULL,
  pwd varchar(128) NOT NULL,
  PRIMARY KEY (username)
) ;

DROP TABLE IF EXISTS user_details;
CREATE TABLE user_details (
  username varchar(128) NOT NULL,
  rname varchar(128) NOT NULL,
  DOB date NOT NULL,
  phone_no char(10) NOT NULL,
  PRIMARY KEY (username),
  FOREIGN KEY (username) REFERENCES login_details(username) ON DELETE CASCADE
);

DROP TABLE IF EXISTS wallet;
CREATE TABLE wallet (
  wallet_id varchar(128) NOT NULL,  
  username varchar(128) NOT NULL,
  current_amt int NOT NULL,
  wallet_type varchar(128) NOT NULL,
  PRIMARY KEY (wallet_id),
  FOREIGN KEY (username) REFERENCES user_details(username) ON DELETE CASCADE
) ;

DROP TABLE IF EXISTS payment_details;
CREATE TABLE payment_details (
  payment_id int NOT NULL AUTO_INCREMENT,  
  sender_wallet_id varchar(128) NOT NULL,
  receiver_wallet_id varchar(128) NOT NULL,
  date_of_payment date NOT NULL,
  amount int NOT NULL,
  payment_status varchar(128) DEFAULT 'completed',
  PRIMARY KEY (payment_id),
  FOREIGN KEY (sender_wallet_id) REFERENCES wallet(wallet_id) ON DELETE CASCADE,
  FOREIGN KEY (receiver_wallet_id) REFERENCES wallet(wallet_id) ON DELETE CASCADE
) ;

DROP TABLE IF EXISTS transaction_details;
CREATE TABLE transaction_details (
  transaction_id int NOT NULL AUTO_INCREMENT,  
  payment_id int NOT NULL,
  wallet_id varchar(128) NOT NULL,
  date_of_transaction date NOT NULL,
  amt int NOT NULL,
  transaction_type varchar(128) NOT NULL,
  transaction_status varchar(128) DEFAULT 'completed',
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (payment_id) REFERENCES payment_details(payment_id) ON DELETE CASCADE,
  FOREIGN KEY (wallet_id) REFERENCES wallet(wallet_id) ON DELETE CASCADE
) ;

DROP TABLE IF EXISTS investment_summary;
CREATE TABLE investment_summary (
  username varchar(128) NOT NULL,
  principal int NOT NULL,
  current_worth int NOT NULL,
  return_value int NOT NULL,
  PRIMARY KEY (username),
  FOREIGN KEY (username) REFERENCES user_details(username) ON DELETE CASCADE
) ;

DROP TABLE IF EXISTS positions;
CREATE TABLE positions (
  fundname varchar(128) NOT NULL,  
  username varchar(128) NOT NULL,
  current_worth decimal NOT NULL,
  bought_at decimal NOT NULL,
  curr_fund_price decimal NOT NULL,
  quantity decimal NOT NULL,
  PRIMARY KEY (username,fundname),
  FOREIGN KEY (username) REFERENCES user_details(username) ON DELETE CASCADE
);

DROP TABLE IF EXISTS return_summary ;
CREATE TABLE return_summary ( 
  serial_no int NOT NULL AUTO_INCREMENT,  
  username varchar(128) NOT NULL,
  return_percentage varchar(128) NOT NULL, 
  date_of_return date NOT NULL DEFAULT now(),
  base_amount int NOT NULL,
  final_amount int NOT NULL,
  PRIMARY KEY (serial_no),
  FOREIGN KEY (username) REFERENCES user_details(username) ON DELETE CASCADE
);

DROP TABLE IF EXISTS reward;
CREATE TABLE reward (
  serial_no int NOT NULL AUTO_INCREMENT,
  date_of_reward date NOT NULL DEFAULT now(),
  reward varchar(128) NOT NULL,  
  username varchar(128) NOT NULL,
  PRIMARY KEY (serial_no),
  FOREIGN KEY (username) REFERENCES user_details(username) ON DELETE CASCADE
) ;

DROP TABLE IF EXISTS question;
CREATE TABLE question (
  username varchar(128) NOT NULL,
  q1 int NOT NULL,
  q2 int NOT NULL,
  q3 int NOT NULL,
  q4 int NOT NULL,
  q5 int NOT NULL,
  q6 int NOT NULL,
  q7 int NOT NULL,
  q8 int NOT NULL,
  q9 int NOT NULL,
  q10 varchar(128) NOT NULL,
  q11 varchar(128) NOT NULL,
  time_stamp TIME NOT NULL DEFAULT now(),
  PRIMARY KEY (username),
  FOREIGN KEY (username) REFERENCES user_details(username) ON DELETE CASCADE
);

DROP TABLE IF EXISTS user_score;
CREATE TABLE user_score (
  username varchar(128) NOT NULL,
  risk_score decimal NOT NULL,
  term_score decimal NOT NULL,
  dept_score decimal NOT NULL,
  cap decimal NOT NULL,
  sectors varchar(128) NOT NULL,
  PRIMARY KEY (username),
  FOREIGN KEY (username) REFERENCES user_details(username) ON DELETE CASCADE
);

DROP TABLE IF EXISTS fund_score;
CREATE TABLE fund_score (
  fundname varchar(128) NOT NULL,
  f_risk_score decimal NOT NULL,
  f_term_score decimal NOT NULL,
  f_dept_score decimal NOT NULL,
  f_cap decimal NOT NULL,
  f_sectors varchar(128) NOT NULL,
  PRIMARY KEY (fundname)
);

DROP TABLE IF EXISTS matchmaking;
CREATE TABLE matchmaking (
  username varchar(128) NOT NULL,
  fundname varchar(128) NOT NULL,
  PRIMARY KEY (username),
  FOREIGN KEY (username) REFERENCES user_details(username) ON DELETE CASCADE,
  FOREIGN KEY (fundname) REFERENCES fund_score(fundname) ON DELETE CASCADE
);

DROP TABLE IF EXISTS etfdata;
create table etfdata (
    etfsymbol varchar(255),
    order_no varchar(10),
    primary key(etfsymbol)
);

DROP TABLE IF EXISTS info;
create table info (
    etfsymbol varchar(255),
    52_Week_Hi varchar(255),
    52_Week_Lo varchar(255),
    AUM varchar(255),
    Leveraged varchar(255),
    Asset_Class varchar(255),
    Asset_Class_Size varchar(255),
    Asset_Class_Style varchar(255),
    Brand varchar(255),
    Category1 varchar(255),
    Category2 varchar(255),
    ETF_Home_Page varchar(255),
    Expense_Ratio varchar(255),
    Focus varchar(255),
    Inception varchar(255),
    Index_Tracked varchar(255),
    Issuer varchar(255),
    Niche varchar(255),
    Price varchar(255),
    General_Region varchar(255),
    Specific_region varchar(255),
    General_Sector varchar(255),
    Specific_Sector varchar(255),
    Segment varchar(255),
    Shares varchar(255),
    Strategy varchar(255),
    Structure varchar(255),
    Weighting_Scheme varchar(255),
    PRIMARY KEY (etfsymbol),
    FOREIGN KEY (etfsymbol) REFERENCES etfdata(etfsymbol) ON DELETE CASCADE
);

DROP TABLE IF EXISTS technicals;
create table technicals(
    etfsymbol varchar(255),
    20_Day_MA varchar(255),
    60_Day_MA varchar(255),
    Average_Spread_dollar varchar(255),
    Average_Spread_percentage varchar(255),
    Lower_Bollinger_10_Day varchar(255),
    Lower_Bollinger_20_Day varchar(255),
    Lower_Bollinger_30_Day varchar(255),
    MACD_100_Period varchar(255),
    MACD_15_Period varchar(255),
    Maximum_Premium_Discount varchar(255),
    Median_Premium_Discount varchar(255),
    RSI_10_Day varchar(255),
    RSI_20_Day varchar(255),
    RSI_30_Day varchar(255),
    Resistance_Level_1 varchar(255),
    Resistance_Level_2 varchar(255),
    Stochastic_Oscillator_D_1Day varchar(255),
    Stochastic_Oscillator_D_5Day varchar(255),
    Stochastic_Oscillator_K_1Day varchar(255),
    Stochastic_Oscillator_K_5Day varchar(255),
    Support_Level_1 varchar(255),
    Support_Level_2 varchar(255),
    Tracking_Difference_Max_Downside varchar(255),
    Tracking_Difference_Max_Upside varchar(255),
    Tracking_Difference_Median varchar(255),
    Ultimate_Oscillator varchar(255),
    Upper_Bollinger_10Day varchar(255),
    Upper_Bollinger_20Day varchar(255),
    Upper_Bollinger_30Day varchar(255),
    Williams_Range_10Day varchar(255),
    Williams_Range_20Day varchar(255),
    5day_volatility varchar(255),
    20day_volatility varchar(255),
    50day_volatility varchar(255),
    200day_volatility varchar(255),
    beta varchar(255),
    standard_deviation varchar(255),
    PRIMARY KEY (etfsymbol),
    FOREIGN KEY (etfsymbol) REFERENCES etfdata(etfsymbol) ON DELETE CASCADE
);

DROP TABLE IF EXISTS performance;
create table performance(
   etfsymbol varchar(255),
   1_Month_Return varchar(10),
   3_Month_Return varchar(10),
   YTD_Return varchar(10),
   1_Year_Return varchar(10),
   3_Year_Return varchar(10),
   5_Year_Return varchar(10),
   PRIMARY KEY (etfsymbol),
   FOREIGN KEY (etfsymbol) REFERENCES etfdata(etfsymbol) ON DELETE CASCADE
);

DROP TABLE IF EXISTS ratings;
create table ratings(
    etfsymbol varchar(255),
    Liquidity varchar(255),
    Expenses varchar(5),
    Performance varchar(5),
    Volatility varchar(5),
    Dividend varchar(5),
    Concentration varchar(5),
    PRIMARY KEY (etfsymbol),
    FOREIGN KEY (etfsymbol) REFERENCES etfdata(etfsymbol) ON DELETE CASCADE
);

CREATE VIEW raw_funds_data  AS SELECT etfdata.etfsymbol , info.Leveraged , info.Asset_Class_Size, info.Price ,info.Specific_Sector , info.General_Sector, technicals.beta,technicals.200day_volatility,technicals.20_Day_MA,technicals.60_Day_MA,technicals.standard_deviation,performance.1_Month_Return,performance.5_Year_Return FROM etfdata,info , technicals , performance WHERE etfdata.etfsymbol = technicals.etfsymbol AND etfdata.etfsymbol = info.etfsymbol AND etfdata.etfsymbol =performance.etfsymbol;
