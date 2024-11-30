INSERT_LOGIN_DETAILS = (
    "INSERT INTO `cash_by_chance`.`login_details`(`username`,`pwd`) VALUES (%s,%s)"
)
INSERT_USER_DETAILS = "INSERT INTO `cash_by_chance`.`user_details`(`username`,`rname`,`DOB`,`phone_no`) VALUES (%s,%s,%s,%s)"
INSERT_INVESTMENT_SUMMARY = "INSERT INTO `cash_by_chance`.`investment_summary`(`username`,`principal`,`current_worth`,`return_value`) VALUES (%s,%s,%s,%s)"
INSERT_WALLET_DETAILS = "INSERT INTO `cash_by_chance`.`wallet`(`username`,`wallet_id`,`current_amt`,`wallet_type`) VALUES (%s,%s,%s,%s)"
INSERT_RETURN_DETAILS = "INSERT INTO `cash_by_chance`.`return_summary`(`username`,`return_percentage`,`base_amount`,`final_amount`) VALUES (%s,%s,%s,%s)"
INSERT_REWARD_DETAILS = (
    "INSERT INTO `cash_by_chance`.`reward`(`username`,`reward`) VALUES (%s,%s)"
)
INSERTION_OF_PAYMENT_DETAILS_NO_STATUS = "INSERT INTO `payment_details`(`sender_wallet_id`,`receiver_wallet_id`, `date_of_payment`, `amount`) VALUES (%s,%s,curdate(),%s)"
INSERT_TRANSACTION_DETAILS_NO_STATUS = "INSERT INTO `transaction_details`(`payment_id`,`wallet_id`,`date_of_transaction`, `amt`, `transaction_type`) VALUES (%s,%s,curdate(),%s,%s)"
INSERT_TRANSACTION_DETAILS_WITH_STATUS = "INSERT INTO `transaction_details`(`payment_id`,`wallet_id`,`date_of_transaction`, `amt`, `transaction_type`, `transaction_status`) VALUES (%s,%s,curdate(),%s,%s,%s)"
INSERT_PAYMENT_DETAILS_WITH_STATUS = "INSERT INTO `payment_details`(`sender_wallet_id`,`receiver_wallet_id`, `date_of_payment`, `amount`, `payment_status`) VALUES (%s,%s,curdate(),%s,%s)"
INSERT_QUESTION_RESPONSES = "INSERT INTO `question`(`username`,`q1`,`q2`,`q3`,`q4`,`q5`,`q6`,`q7`,`q8`,`q9`,`q10`,`q11`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

GET_LOGIN_DETAILS = "SELECT * FROM `login_details` WHERE (`username`=%s)"
GET_LOGIN_DETAILS_WITH_PASSWORD = (
    "SELECT * FROM `login_details` WHERE (`username`=%s) AND (`pwd`=%s)"
)
POSITION_INFORMATION = "SELECT * FROM `positions` WHERE (`username` = %s)"
RETURN_INFORMATION = "SELECT * FROM `return_summary` WHERE (`username`=%s)"
GET_USER_TRANSACTION_DETAILS = (
    "SELECT * FROM `transaction_details` WHERE (`wallet_id` =%s OR `wallet_id` =%s)"
)
GET_WALLET_AMOUNT = "SELECT `current_amt` FROM `wallet` WHERE (`wallet_id`=%s)"
GET_NAME = "SELECT `rname` FROM `user_details` WHERE (`username`=%s)"
FETCH_PAYMENT_ID = "SELECT `payment_id` FROM `payment_details` WHERE (`sender_wallet_id`=%s) AND (`receiver_wallet_id`=%s) AND (`date_of_payment`=curdate()) AND (`amount`=%s)"

UPDATE_WALLET_AMOUNT = "UPDATE `wallet` SET `current_amt`=%s WHERE `wallet_id`= %s"
