import logging

from database import DatabaseConnectionManager
from query import *

cursor = DatabaseConnectionManager.get_cursor()


def update_fundprice(user_uname):
    """
    Thif function updates the current fund price in the positions table

    Parameters:
        user_uname: username of the user
    """
    username = (user_uname,)  # get list of all funds in positions table
    cursor.execute(GET_FUNDNAME, username)
    fundlist = cursor.fetchall()
    for fund in fundlist:  # updating curr price of all funds in positions
        fundname = fund[0]

        fund_name = (fundname,)
        cursor.execute(GET_PRICE, fund_name)
        currprice = cursor.fetchall()[0][0]
        user_fund_info = (currprice, fundname, user_uname)
        cursor.execute(UPDATE_POSITION, user_fund_info)
        DatabaseConnectionManager.commit_transaction()


def update_live(user_uname):
    """
    This function updates current worth from positions table in the investment summary table.

    Parameters:
        user_uname: username of the user
    """
    username = (user_uname,)
    cursor.execute(GET_CURR_WORTH, username)
    total_worth = cursor.fetchall()[0][0]

    totalworth_user = (total_worth, user_uname)
    cursor.execute(UPDATE_INVESTMENT_SUMMARY, totalworth_user)
    DatabaseConnectionManager.commit_transaction()


def update_return_summary(user_uname):
    """
    This function updates the return summary for a user.

    Parameters:
        user_uname: username of the user
    """
    username = (user_uname,)
    cursor.execute(GET_INVESTMNT_INFO, username)
    result = cursor.fetchall()  # current worth
    # rename x
    for x in result:
        total_return = x[0]
        principal = x[1]
    if principal != 0:
        return_per = (total_return / float(principal)) * 100.0
    else:
        return_per = 0

    investment_summary_ofuser = (user_uname, return_per, principal, total_return)
    cursor.execute(INSERT_INTO_RETURN_SUMMARY, investment_summary_ofuser)
    DatabaseConnectionManager.commit_transaction()


cursor.execute(GET_USERNAMES)
allusers = cursor.fetchall()


for user in allusers:
    # bythis currprice in positions table updated
    update_fundprice(user[0])
# by this currworth using currprice and quantity updated
cursor.execute(UPDATE_POSITIONS)


for user in allusers:
    # updates current worth of all users in investment_summary table
    update_live(user[0])
# updates return-value of all users in investment_summary table
cursor.execute(UPDATE_INVESTMNT_SUMMARY)


for user in allusers:
    # updates return_summary table by calc return percentage
    update_return_summary(user[0])

logging.info(
    "current price, current worth and return summary were all updated successfully"
)
