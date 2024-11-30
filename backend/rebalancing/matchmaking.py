import logging
import math
import operator

import mysql.connector as MSQC

from database import DatabaseConnectionManager
from query import *

cursor = DatabaseConnectionManager.get_cursor()

# matchmaking for each user
cursor.execute(GET_USERNAMES)
user_list = cursor.fetchall()

for curr_user in user_list:
    try:

        curr_uname = curr_user[0]
        username = (curr_uname,)
        cursor.execute(GET_USERSCORE_INFO, username)
        user = cursor.fetchall()

        risk_score = float(user[0][1])
        term_score = float(user[0][2])
        dept_score = float(user[0][3])
        cap_score = float(user[0][4])
        sectors = str(user[0][5])

        distances = []

        sectors_list = sectors.split(",")
        for curr_sector in sectors_list:
            val = (str(curr_sector),)
            if val[0].strip() == "":
                val = ("None",)
            cursor.execute(GET_FUND_INFO, val)
            res = cursor.fetchall()

            # KNN with k = 1
            k = 1
            for i in range(len(res)):
                fund_name = res[i][0]
                # rename f_risk_score to fund_risk_score if f means fund
                f_risk_score = float(res[i][1])
                f_term_score = float(res[i][2])
                f_dept_score = float(res[i][3])
                f_cap = float(res[i][4])
                curr_dist = math.sqrt(
                    (risk_score - f_risk_score) * (risk_score - f_risk_score)
                    + (term_score - f_term_score) * (term_score - f_term_score)
                    + (dept_score - f_dept_score) * (dept_score - f_dept_score)
                    + (cap_score - f_cap) * (cap_score - f_cap)
                )
                distances.append([curr_dist, fund_name])

        distances.sort(key=operator.itemgetter(0))
        selected_fund = distances[0]
        selected_fund_name = selected_fund[1]

        try:
            val = (curr_uname, selected_fund_name, selected_fund_name)
            cursor.execute(INSERT_INTO_MATCHMAKING, val)
            DatabaseConnectionManager.commit_transaction()
        except Exception as e:
            logging.error("Error in inserting into matchmaking table", exc_info=True)

    except Exception as e:
        logging.error(
            "Error in fetching and/or processing user/fund scores", exc_info=True
        )

logging.info(
    "users were successfully mapped to funds and inserted into matchmaking table"
)
