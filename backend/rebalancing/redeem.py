import logging
from datetime import date

from database import DatabaseConnectionManager
from query import *

cursor = DatabaseConnectionManager.get_connection().cursor(buffered=True)
curr_date = date.today()


def withdraw(user, walletid, wallet_id_main, withd_amt):
    """
    This function handles all changes in the table whenever withdraw transaction is requested from deposit wallet.
    Parameter:
        user: This depicts the current user name.
        walletid: This is the main wallet id of the user.
        withd_amt: The amount to be withdrawn.
    """
    username = (user,)
    cursor.execute(GET_INVESTMENT_SUMMARY_INFO, username)

    investment_info = cursor.fetchall()  # current worth
    for x in investment_info:
        curr_worth = x[0]
        principal = x[1]

    if curr_worth < withd_amt:
        transaction_info = ("failed", walletid, "Credit", curr_date, "processing")
        cursor.execute(UPDATE_TRANSACTION_DETAILS, transaction_info)
        payment_info = ("failed", walletid, curr_date, "processing")
        cursor.execute(UPDATE_PAYMENT_DETAILS, payment_info)
        DatabaseConnectionManager.commit_transaction()
    else:

        wallet_info = (withd_amt, username[0], "main")
        cursor.execute(UPDATE_MAIN_WALLET, wallet_info)
        pay_info = ("completed", walletid, curr_date, "processing")
        cursor.execute(UPDATE_PAYMENT_DETAILS, pay_info)
        # add_credit = (wallet_id_main,curr_date,withd_amt,'Credit','completed')
        # cursor.execute(ADD_CREDIT_TO_TRANSACTION,add_credit)
        transac_info = ("completed", walletid, "Credit", curr_date, "processing")
        cursor.execute(UPDATE_TRANSACTION_DETAILS, transac_info)

        percentage = float(withd_amt) / float(curr_worth)
        print(percentage)
        principal = float(principal) - float(float(principal) * percentage)
        # update investment_summary
        cursor.execute(GET_RETURN_VALUE, username)
        initial_return = cursor.fetchall()[0][0]
        investment_figures = (
            principal,
            float(curr_worth) - withd_amt,
            float(curr_worth) - principal - withd_amt,
            user,
        )
        cursor.execute(UPDATE_INVESTMENT_SUMMARY_REDEEM, investment_figures)
        DatabaseConnectionManager.commit_transaction()
        cursor.execute(GET_RETURN_VALUE, username)
        return_value = cursor.fetchall()[0][0]
        DatabaseConnectionManager.commit_transaction()
        if withd_amt - return_value < 0:
            # update reward
            reward_info = (abs(initial_return - return_value), user)
            cursor.execute(INSERT_INTO_REWARD, reward_info)
            DatabaseConnectionManager.commit_transaction()
        else:
            reward_info_when_loss = (0, user)
            cursor.execute(INSERT_INTO_REWARD, reward_info_when_loss)
            DatabaseConnectionManager.commit_transaction()

        cursor.execute(GET_POSITIONS)
        count = cursor.fetchone()[0]
        worth = float(withd_amt) / float(count)
        user_worth = (worth, user)
        cursor.execute(UPDATE_POSITIONS_REDEEM, user_worth)
        DatabaseConnectionManager.commit_transaction()


cursor.execute(GET_USERS)
allusers = cursor.fetchall()
for user in allusers:
    id = ""
    id = user[0].split("@")[0]
    user_id = id + ".main"
    user_idm = id + ".deposit"

    val1 = (user_idm, "Credit", curr_date)
    cursor.execute(GET_TOTAL_CREDIT, val1)

    credit = cursor.fetchall()[0][0]
    val2 = (user_idm, "Debit", curr_date)
    cursor.execute(GET_TOTAL_DEBIT, val2)

    debit = cursor.fetchall()[0][0]
    if debit == None:
        debit = 0
    if credit == None:
        credit = 0

    finaldeposit_amt = float(credit) - float(debit)
    if finaldeposit_amt < 0:
        withdraw(user[0], user_idm, user_id, abs(finaldeposit_amt))

logging.info(
    "rewards and positions were calcualated and withdrawal was completed successfully"
)
