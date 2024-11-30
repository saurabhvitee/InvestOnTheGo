import logging

from database import DatabaseConnectionManager
from query import *

cursor = DatabaseConnectionManager.get_cursor()

# info regarding the cap of funds
large_cap_weight = 0.5
mid_cap_weight = 1
small_cap_weight = 2
large_caps = ["apple", "amazon", "nestle", "samsung"]
mid_caps = ["axon", "pinterest", "synopsis", "reliance_steel_aluminium"]
small_caps = ["crocs", "american_airlines", "tsmc"]
total_cap_value = (
    (large_cap_weight * len(large_caps))
    + (mid_cap_weight * len(mid_caps))
    + (small_cap_weight * len(small_caps))
)

cursor.execute(GET_USERNAMES)
user_list = cursor.fetchall()

for curr_user in user_list:
    username = curr_user[0]

    try:

        user = (username,)
        cursor.execute(GET_QUES_INFO, user)
        user_question = cursor.fetchall()

        q1 = float(user_question[0][1])
        q2 = float(user_question[0][2])
        q3 = float(user_question[0][3])
        q4 = float(user_question[0][4])
        q5 = float(user_question[0][5])
        q6 = float(user_question[0][6])
        q7 = float(user_question[0][7])
        q8 = float(user_question[0][8])
        q9 = float(user_question[0][9])
        # assuming that it is a comma separated list of companies selected
        # q10 is cap question
        q10 = user_question[0][10]
        # assuming that it is a comma separated list of sectors selected
        # q11 is sectors question
        q11 = user_question[0][11]

        # assuming q1, q2 ... store the score associated with the choice the user seleceted in the questionarre
        risk_score = (q1 + q2 + q3 + q4 + q5) / 5
        term_score = (q6 + q7) / 2
        dept_score = (q8 + q9) / 2
        sectors = q11

        cap = 0.0
        caps_chosen = q10.split(",")
        for curr_cap in caps_chosen:
            if curr_cap in large_caps:
                cap += large_cap_weight
            else:
                if curr_cap in mid_caps:
                    cap += mid_cap_weight
                else:
                    cap += small_cap_weight
        cap = (cap / total_cap_value) * 10

        SCORES = (
            str(username),
            str(risk_score),
            str(term_score),
            str(dept_score),
            str(cap),
            str(sectors),
            str(risk_score),
            str(term_score),
            str(dept_score),
            str(cap),
            str(sectors),
        )

        cursor.execute(INSERT_USERSCORES, SCORES)
        DatabaseConnectionManager.commit_transaction()
    except Exception as e:
        logging.error(
            "Error in fetching user's questionarre responses and storing calculated scores in DB",
            exc_info=True,
        )

logging.info("scores were successfully updated")
