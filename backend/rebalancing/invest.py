import logging
from datetime import date

import mysql.connector as MSQC

from database import DatabaseConnectionManager
from query import *

cursor = DatabaseConnectionManager.get_cursor()

cursor.execute(GET_USERNAMES)
user_list = cursor.fetchall()
curr_date = date.today()

for user in user_list:
    curr_user = str(user[0])

    val = (curr_user, "deposit")
    cursor.execute(GET_WALLET_ID, val)
    res = cursor.fetchall()
    deposit_wallet = res[0][0]

    val = (deposit_wallet, curr_date)
    cursor.execute(GET_TRANSACTION_DETAILS, val)

    try:
        deposit_list = cursor.fetchall()
    except:
        continue

    total_deposit_amt = 0

    for deposit in deposit_list:
        amount = int(deposit[0])
        if str(deposit[1]).lower() == "credit":
            total_deposit_amt += amount
        else:
            total_deposit_amt -= amount

    username = (curr_user,)
    cursor.execute(GET_MATCHED_FUND, username)
    matched_fund = cursor.fetchall()
    fund_name = matched_fund[0][0]

    # fund price
    val = (fund_name,)
    cursor.execute(GET_PRICE, val)
    matched_price = cursor.fetchall()
    price = float(matched_price[0][0])

    if total_deposit_amt > 0:

        # change status of debit transactions from deposit to 'completed'
        val = (deposit_wallet, curr_date)
        cursor.execute(UPDATE_DEBIT_TRANSACTION_STATUS, val)

        # initialize values
        buy_quantity = float(total_deposit_amt) / price
        curr_worth = 0.0
        spent_amt = 0.0
        net_quantity = 0.0
        net_worth = 0.0
        net_spent_amt = 0.0

        val = (curr_user, fund_name)
        cursor.execute(GET_CURR_POSITION, val)
        try:
            res = cursor.fetchall()
            curr_quantity = float(res[0][5])
            present_worth = float(res[0][2])
            present_bought_at = float(res[0][3])

            net_quantity = curr_quantity + buy_quantity
            net_worth = net_quantity * price
            net_spent_amt = present_bought_at + total_deposit_amt
        except:
            # no records found for this user, fund combination
            curr_worth = buy_quantity * price
            spent_amt = total_deposit_amt
            net_quantity = buy_quantity
            net_worth = curr_worth
            net_spent_amt = spent_amt

        try:
            val = (
                fund_name,
                curr_user,
                buy_quantity,
                curr_worth,
                spent_amt,
                price,
                net_quantity,
                net_worth,
                net_spent_amt,
                price,
            )
            cursor.execute(INSERT_INTO_POSITIONS, val)
            logging.info("values inserted into positions table successfully")
            DatabaseConnectionManager.commit_transaction()
        except Exception as e:
            logging.error("Error in inserting into positions table", exc_info=True)

logging.info("matched funds were successfully fetched and invested in")
