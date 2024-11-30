GET_USERNAMES = "SELECT username FROM `login_details`"
GET_QUES_INFO = "SELECT * FROM `question` WHERE `username`= %s"
INSERT_USERSCORES = "INSERT INTO `cash_by_chance`.`user_score`(`username`,`risk_score`,`term_score`,`dept_score`,`cap`,`sectors`) VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE `risk_score`= %s, `term_score`= %s, `dept_score`= %s, `cap`= %s, `sectors`= %s"
GET_WALLET_ID = (
    "SELECT wallet_id FROM `wallet` WHERE `username`=%s AND `wallet_type`=%s"
)
GET_TRANSACTION_DETAILS = "SELECT amt, transaction_type FROM `transaction_details` WHERE wallet_id=%s AND date_of_transaction=%s"
GET_MATCHED_FUND = "SELECT fundname FROM `matchmaking` WHERE `username`=%s"
GET_PRICE = "SELECT price FROM `info` WHERE etfsymbol=%s"
UPDATE_DEBIT_TRANSACTION_STATUS = "UPDATE transaction_details SET transaction_status = 'completed' WHERE wallet_id =%s AND transaction_type = 'debit' AND date_of_transaction =%s AND transaction_status = 'processing' "
GET_CURR_POSITION = "SELECT * FROM `positions` WHERE username=%s AND fundname=%s"
INSERT_INTO_POSITIONS = "INSERT INTO `positions`(`fundname`,`username`,`quantity`,`current_worth`,`bought_at`,`curr_fund_price`) VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE `quantity`= %s, `current_worth`= %s, `bought_at`= %s, `curr_fund_price`= %s"
GET_USERSCORE_INFO = "SELECT * FROM `user_score` WHERE (`username`= %s)"
GET_FUND_INFO = (
    "SELECT * FROM `fund_score` WHERE (`f_sectors`=%s) OR `f_sectors`='None' "
)
INSERT_INTO_MATCHMAKING = "INSERT INTO `matchmaking`(`username`,`fundname`) VALUES (%s,%s) ON DUPLICATE KEY UPDATE `fundname`= %s"
GET_INVESTMENT_SUMMARY_INFO = (
    "SELECT current_worth, principal FROM investment_summary WHERE username = %s"
)
UPDATE_TRANSACTION_DETAILS = "UPDATE transaction_details SET transaction_status = %s WHERE wallet_id =%s AND transaction_type =%s AND date_of_transaction = %s AND transaction_status = %s  "
UPDATE_PAYMENT_DETAILS = "UPDATE payment_details SET payment_status = %s WHERE receiver_wallet_id= %s AND date_of_payment = %s AND payment_status = %s"
UPDATE_INVESTMENT_SUMMARY_REDEEM = " UPDATE investment_summary SET principal = %s, current_worth = %s, return_value = %s  where username = %s"
GET_RETURN_VALUE = "SELECT return_value FROM investment_summary WHERE username = %s"
INSERT_INTO_REWARD = (
    "INSERT INTO reward (date_of_reward,reward,username) VALUES (curdate(),%s,%s)"
)
GET_POSITIONS = "SELECT COUNT(*) FROM positions"
UPDATE_POSITIONS_REDEEM = (
    " UPDATE positions SET current_worth = current_worth - %s WHERE username = %s"
)
GET_USERS = "SELECT username FROM user_details"
GET_TOTAL_DEBIT = "SELECT SUM(amt) FROM transaction_details WHERE wallet_id= %s and transaction_type=%s AND date_of_transaction = %s"
GET_TOTAL_CREDIT = "SELECT SUM(amt) FROM transaction_details WHERE wallet_id= %s and transaction_type= %s AND date_of_transaction =%s"
GET_FUNDNAME = "SELECT fundname from positions WHERE username = %s"
GET_PRICE = "SELECT price FROM info WHERE etfsymbol=%s"
UPDATE_POSITION = (
    "UPDATE positions SET curr_fund_price =%s WHERE fundname =%s AND username=%s"
)
GET_CURR_WORTH = "SELECT SUM(current_worth) FROM positions WHERE username= %s"
UPDATE_INVESTMENT_SUMMARY = (
    "UPDATE investment_summary SET current_worth = %s WHERE username = %s"
)

GET_INVESTMNT_INFO = (
    "SELECT return_value, principal FROM investment_summary WHERE username = %s"
)
INSERT_INTO_RETURN_SUMMARY = "INSERT INTO return_summary (username, return_percentage, date_of_return,base_amount,final_amount) VALUES (%s,%s,curdate(),%s,%s)"
UPDATE_POSITIONS = "UPDATE positions SET current_worth = quantity * curr_fund_price"
UPDATE_INVESTMNT_SUMMARY = (
    "UPDATE investment_summary SET return_value= current_worth - principal"
)
GET_FUNDS = "SELECT * FROM raw_funds_data LIMIT 100"
INSERT_INTO_FUND_SCORE = "INSERT INTO `cash_by_chance`.`fund_score`(`fundname`,`f_risk_score`,`f_term_score`,`f_dept_score`,`f_cap`,`f_sectors`) VALUES (%s,%s,%s,%s,%s,%s)"
DEL_FUND_SCORE = "DELETE FROM fund_score WHERE 1=1"
UPDATE_MAIN_WALLET = "UPDATE wallet SET current_amt = current_amt + %s WHERE username = %s AND wallet_type = %s"
ADD_CREDIT_TO_TRANSACTION = " INSERT  INTO transaction_details (wallet_id, date_of_transaction, amt, transaction_type, transaction_status) VALUES (%s,%s,%s,%s,%s)"
RECONCILIATION_OF_TRANSACTION = (
    "UPDATE transaction_details SET transaction_status =%s WHERE transaction_status= %s"
)
