from fastapi import HTTPException

import validations
from config import *
from DAO import *
from database import *
from queries import *
from utils import *


def make_deposit_payment(
    uname, sender_mainwallet_id, sender_depositwallet_id, amt_to_pay
):
    """
    This function is used to transfer amount from a user's main wallet to
    their deposit wallet.

    Parameters:
        uname: sender's username
        sender_mainwallet_id: sender's main wallet ID
        sender_depositwallet_id: sender's deposit wallet ID
        amt_to_pay: amount that needs to be paid
    """
    validations.validate_amt(amt_to_pay)
    curr_user = UserInfoDao(uname)
    res1, res2 = curr_user.get_wallet_amt(sender_mainwallet_id, sender_depositwallet_id)
    sender_bal = int(res1[0][0])
    sender_deposit_bal = int(res2[0][0])

    DatabaseConnectionManager.start_transaction()

    try:
        curr_wallet = WalletInfoDao()
        curr_wallet.update_wallet_amount(sender_bal - amt_to_pay, sender_mainwallet_id)
        curr_wallet.update_wallet_amount(
            sender_deposit_bal + amt_to_pay, sender_depositwallet_id
        )

        curr_payment = PaymentInfoDao(uname)
        curr_payment.inserting_payment_details_nostatus(
            sender_mainwallet_id, sender_depositwallet_id, amt_to_pay
        )

        queryresult = curr_payment.get_payment_id(
            sender_mainwallet_id, sender_depositwallet_id, amt_to_pay
        )
        paymentID = queryresult[len(queryresult) - 1][0]

        curr_transaction = TransactionInfoDao(uname)
        curr_transaction.insert_transactiondetails_nostatus(
            str(paymentID), sender_mainwallet_id, str(amt_to_pay), DEBIT_TYPE
        )
        curr_transaction.insert_transactiondetails_nostatus(
            str(paymentID), sender_depositwallet_id, str(amt_to_pay), CREDIT_TYPE
        )

        DatabaseConnectionManager.commit_transaction()

        return {
            "success": "True",
            "message": "Payment Successful",
            "curr_main_amt": sender_bal,
            "curr_dep_amt": sender_deposit_bal,
        }

    except:
        DatabaseConnectionManager.rollback_transaction()
        raise HTTPException(
            status_code=500,
            detail="Payment was unsuccessful. Original wallet balance has been restored.",
        )


def make_payment_from_wallet(
    uname, sender_mainwallet_id, receiver_mainwallet_id, amt_to_pay
):
    """
    This function is used to make a payment from a user's wallet.

    Parameters:
        uname: sender's username
        sender_mainwallet_id: sender's main wallet ID
        receiver_mainwallet_id: receiver's main wallet ID
        amt_to_pay: amount that needs to be paid
    """

    # should this be two try except to catch different exceptions I AM SO CONFUSED

    validations.validate_amt(amt_to_pay)

    sender_mainwallet_id, sender_depositwallet_id = generate_wallet_names(uname)

    curr_user = UserInfoDao(uname)
    res1, res2 = curr_user.get_wallet_amt(sender_mainwallet_id, sender_depositwallet_id)
    sender_bal = int(res1[0][0])
    sender_deposit_bal = int(res2[0][0])

    validations.validate_balance(sender_bal, amt_to_pay)

    if amt_to_pay % 10 == 0:
        to_deposit = (amt_to_pay * DEPOSIT_PERCENTAGE) // 100
    else:
        to_deposit = 10 - (amt_to_pay % 10)

    sender_bal = sender_bal - amt_to_pay

    if sender_bal < to_deposit:
        to_deposit = sender_bal
        sender_bal = 0
    else:
        sender_bal = sender_bal - to_deposit

    sender_deposit_bal += to_deposit
    DatabaseConnectionManager.start_transaction()

    try:
        curr_wallet = WalletInfoDao()
        res, _ = curr_user.get_wallet_amt(
            receiver_mainwallet_id, sender_depositwallet_id
        )
        receiver_bal = int(res[0][0])

        receiver_bal = receiver_bal + amt_to_pay

        curr_wallet.update_wallet_amount(sender_bal, sender_mainwallet_id)
        curr_wallet.update_wallet_amount(sender_deposit_bal, sender_depositwallet_id)
        curr_wallet.update_wallet_amount(receiver_bal, receiver_mainwallet_id)

        curr_payment = PaymentInfoDao(uname)
        curr_payment.inserting_payment_details_nostatus(
            sender_mainwallet_id, receiver_mainwallet_id, amt_to_pay
        )

        queryresult = curr_payment.get_payment_id(
            sender_mainwallet_id, receiver_mainwallet_id, amt_to_pay
        )
        paymentID = queryresult[len(queryresult) - 1][0]

        curr_transaction = TransactionInfoDao(uname)
        curr_transaction.insert_transactiondetails_nostatus(
            str(paymentID),
            sender_mainwallet_id,
            str(amt_to_pay + to_deposit),
            DEBIT_TYPE,
        )
        curr_transaction.insert_transactiondetails_nostatus(
            str(paymentID), receiver_mainwallet_id, str(amt_to_pay), CREDIT_TYPE
        )
        curr_transaction.insert_transactiondetails_nostatus(
            str(paymentID), sender_depositwallet_id, str(to_deposit), CREDIT_TYPE
        )

        DatabaseConnectionManager.commit_transaction()

        return {
            "success": "True",
            "message": "Payment Successful",
            "curr_main_amt": sender_bal,
            "curr_dep_amt": sender_deposit_bal,
        }

    except:
        DatabaseConnectionManager.rollback_transaction()
        raise HTTPException(
            status_code=500,
            detail="Payment was unsuccessful. Original wallet balance has been restored.",
        )


def withdrawing_from_deposit_wallet(username, amt_to_wthdrw):
    """
    This function allows the user to withdraw from their deposit wallet when they want to take their savings out.

    Parameters:
        username: user's username
        rname: user's name
        amt_to_wthdrw: the amount the user wants to withdraw from their deposit wallet
    """
    main_wallet_id, deposit_wallet_id = generate_wallet_names(username)
    validations.validate_amt(amt_to_wthdrw)

    curr_user = UserInfoDao(username)
    main_wallet_amount, deposit_wallet_amount = curr_user.get_wallet_amt(
        main_wallet_id, deposit_wallet_id
    )
    user_mainwallet_bal = int(main_wallet_amount[0][0])
    user_deposit_bal = int(deposit_wallet_amount[0][0])

    validations.validate_balance(user_deposit_bal, amt_to_wthdrw)

    user_deposit_bal = user_deposit_bal - amt_to_wthdrw

    DatabaseConnectionManager.start_transaction()
    try:
        curr_wallet = WalletInfoDao()
        curr_wallet.update_wallet_amount(user_deposit_bal, deposit_wallet_id)

        curr_payment = PaymentInfoDao(username)
        curr_payment.inserting_payment_details_with_status(
            deposit_wallet_id, main_wallet_id, str(amt_to_wthdrw)
        )

        fetch_payment_id_result = curr_payment.get_payment_id(
            deposit_wallet_id, main_wallet_id, amt_to_wthdrw
        )
        paymentID = fetch_payment_id_result[len(fetch_payment_id_result) - 1][0]

        curr_transaction = TransactionInfoDao(username)
        curr_transaction.insert_transactiondetails_nostatus(
            str(paymentID), deposit_wallet_id, amt_to_wthdrw, DEBIT_TYPE
        )
        curr_transaction.insert_transactiondetails_with_status(
            str(paymentID), main_wallet_id, amt_to_wthdrw, CREDIT_TYPE
        )
        DatabaseConnectionManager.commit_transaction()
        return {
            "success": "True",
            "message": "Payment Successful",
            "curr_main_amt": user_mainwallet_bal,
            "curr_dep_amt": user_deposit_bal,
        }

    except:
        DatabaseConnectionManager.rollback_transaction()
        raise HTTPException(
            status_code=500,
            detail="Withdrawal from deposit wallet failed. Original balance has been restored.",
        )
