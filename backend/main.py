import hashlib
import logging

from fastapi import Depends, FastAPI, HTTPException

import validations
from auth import UserInfoResolver, signJWT
from config import *
from cors import enable_cors_for_react_ui
from DAO import *
from database import DatabaseConnectionManager
from models import *
from queries import *
from services import *
from utils import *

app = FastAPI()


enable_cors_for_react_ui(app)


@app.post("/v1/register", tags=["details"])
def register(reg_item: RegisterItem):

    """
    This function helps the user to register themselves.
    """

    username = reg_item.username
    curr_pwd = reg_item.password
    hashed_pwd = (hashlib.sha256(curr_pwd.encode())).hexdigest()
    first_name = reg_item.first_name
    phone_num = reg_item.phone_no
    date_of_birth = reg_item.DOB
    main_wallet, deposit_wallet = generate_wallet_names(username)

    DatabaseConnectionManager.start_transaction()

    try:
        curr_user = RegistrationDAO(username)
        curr_user.create_user(hashed_pwd, first_name, date_of_birth, phone_num)
        curr_user.create_investment_summary()
        curr_user.create_user_wallet(main_wallet, deposit_wallet)
        curr_user.create_returns()
        curr_user.create_rewards()

        logging.debug("User registration completed succesfully")
        DatabaseConnectionManager.commit_transaction()
        tokenVal = signJWT(username)["access_token"]
        return {
            "success": "True",
            "message": "Registeration Successful!",
            "uname": username,
            "curr_main_amt": INIT_MAIN_AMT,
            "curr_dep_amt": INIT_DEP_AMT,
            "wallet1_id": main_wallet,
            "wallet2_id": deposit_wallet,
            "tokenVal": tokenVal,
        }
    except:
        DatabaseConnectionManager.rollback_transaction()
        raise HTTPException(status_code=500, detail="Failed to register user")


@app.post("/v1/login", tags=["details"])
def user_login(login_item: LoginItem):

    """
    This function helps the user to login once they've been registered.
    """

    username = login_item.username
    current_password = login_item.password
    hashed_pwd = (hashlib.sha256(current_password.encode())).hexdigest()
    main_wallet, deposit_wallet = generate_wallet_names(username)

    try:
        curr_user = UserInfoDao(username)
        curr_user.get_login_details()
        curr_user.get_loginpwd_details(hashed_pwd)
        name_result = curr_user.get_name_of_user()
        main_amount_res, deposit_amount_res = curr_user.get_wallet_amt(
            main_wallet, deposit_wallet
        )
        tokenVal = signJWT(username)["access_token"]
        return {
            "success": "True",
            "message": "Successful Login",
            "rname": name_result[0],
            "uname": username,
            "curr_main_amt": main_amount_res[0],
            "curr_dep_amt": deposit_amount_res[0],
            "wallet1_id": main_wallet,
            "wallet2_id": deposit_wallet,
            "tokenVal": tokenVal,
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail="User login failed") from e


@app.post("/v1/check/wallet/balance", tags=["details"])
def checking_wallet_balance(walletitem: WalletItem, user=Depends(UserInfoResolver())):
    """
    This function serves the purpose of checking a user's main and deposit wallet's balance.
    """

    main_wallet, deposit_wallet = generate_wallet_names(user.username)
    curr_wallet = UserInfoDao(user.username)
    sender_balance, sender_deposit_balance = curr_wallet.get_wallet_amt(
        main_wallet, deposit_wallet
    )
    logging.debug("wallet balance was successfully fetched")
    return {
        "success": "True",
        "message": "Payment Successful",
        "curr_main_amt": sender_balance,
        "curr_dep_amt": sender_deposit_balance,
    }


@app.post("/v1/dashboard/wallet", tags=["details"])
def withdraw_from_mainwallet(walletitem: WalletItem, user=Depends(UserInfoResolver())):
    """
    This function allows the user to make payments from their wallet to other user's wallet.
    """

    uname = walletitem.username
    validations.validate_uname(user, uname)
    sender_mainwallet_id = walletitem.sender_id
    receiver_mainwallet_id = walletitem.receiver_id
    amt_to_pay = walletitem.amount
    main_wallet, deposit_wallet = generate_wallet_names(uname)
    if receiver_mainwallet_id == deposit_wallet:
        make_deposit_payment(uname, main_wallet, deposit_wallet, amt_to_pay)
    elif sender_mainwallet_id != receiver_mainwallet_id:
        make_payment_from_wallet(
            uname, sender_mainwallet_id, receiver_mainwallet_id, amt_to_pay
        )

    curr_wallet = UserInfoDao(uname)
    sender_balance, sender_deposit_balance = curr_wallet.get_wallet_amt(
        main_wallet, deposit_wallet
    )
    return {
        "success": "True",
        "message": "Payment Successful",
        "curr_main_amt": sender_balance,
        "curr_dep_amt": sender_deposit_balance,
    }


@app.post("/v1/dashboard/wallet/withdraw", tags=["details"])
def withdraw_from_depositwallet(
    deposit_withdraw_item: DepositWithdrawItem, user=Depends(UserInfoResolver())
):
    """
    This function helps a user to withdraw money back from their deposit wallet.
    """

    username = deposit_withdraw_item.username
    validations.validate_uname(user, username)
    amt_to_wthdrw = deposit_withdraw_item.amount
    logging.debug("amount was successfully withdrawn from wallet")
    return withdrawing_from_deposit_wallet(username, amt_to_wthdrw)


@app.get("/v1/history/{uname}")
def get_history_for_user(uname, user=Depends(UserInfoResolver())):
    """
    This function serves the purpose of getting the transaction history of a user.
    """

    validations.validate_uname(user, uname)
    try:
        curr_transaction = TransactionInfoDao(uname)
        transaction_details = curr_transaction.fetch_transaction_details()
        return transaction_details
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="user History could not be fetched"
        ) from e


@app.get("/v1/returns/profit/{uname}")
def get_profits(uname, user=Depends(UserInfoResolver())):
    """
    This function fetches the profits a user has made against their transactions.
    """

    validations.validate_uname(user, uname)
    try:
        curr_returns = ReturnsInfoDao(uname)
        returnInfoOfUser = curr_returns.get_returns_info()
        returnStore = []
        for returnParticular in returnInfoOfUser:
            returnStore.append(
                {
                    "Month": returnParticular[3],
                    "profit": returnParticular[2],
                    "baseamount": returnParticular[4],
                    "finalamount": returnParticular[5],
                }
            )
        return returnStore
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="returns could not be fetched"
        ) from e


@app.get("/v1/returns/allocation/{uname}")
def get_portfolio_allocation(uname, user=Depends(UserInfoResolver())):
    """
    This function fetches the portfolio of different ETFs where a user's money has been invested.
    """

    validations.validate_uname(user, uname)
    try:
        curr_position = PositionInfoDao(uname)
        positionInfoOfUser = curr_position.insert_position_info()
        positionStore = []
        for positionParticular in positionInfoOfUser:
            positionStore.append(
                {"name": positionParticular[0], "amount": positionParticular[2]}
            )
        return positionStore

    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Portfolio of user could not be fetched"
        ) from e


@app.post("/v1/question")
def questions(questionItem: QuestionItem, user=Depends(UserInfoResolver())):
    """
    This function stores the answers to the questionnaire filled by the user in order to match him with funds.
    """

    username = questionItem.username
    validations.validate_uname(user, username)
    question_one_response = questionItem.q1
    question_two_response = questionItem.q2
    question_three_response = questionItem.q3
    question_four_response = questionItem.q4
    question_five_response = questionItem.q5
    question_six_response = questionItem.q6
    question_seven_response = questionItem.q7
    question_eight_response = questionItem.q8
    question_nine_response = questionItem.q9
    question_ten_response = questionItem.q10
    question_eleven_response = questionItem.q11
    question_ten_response = set(question_ten_response)
    question_eleven_response = set(question_eleven_response)
    question_ten_strings = ",".join(question_ten_response)
    question_eleven_strings = ",".join(question_eleven_response)
    DatabaseConnectionManager.start_transaction()

    try:
        curr_question = QuestionInfoDao(username)
        curr_question.insert_questions_responses(
            question_one_response,
            question_two_response,
            question_three_response,
            question_four_response,
            question_five_response,
            question_six_response,
            question_seven_response,
            question_eight_response,
            question_nine_response,
            question_ten_strings,
            question_eleven_strings,
        )

        DatabaseConnectionManager.commit_transaction()
        return {"success": "True", "message": "Successful entry in database!"}
    except Exception as e:
        DatabaseConnectionManager.rollback_transaction()
        raise HTTPException(
            status_code=500,
            detail="Question Responses could not be stored in the database",
        ) from e
