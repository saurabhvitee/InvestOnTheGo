from fastapi import HTTPException

from models import *


def validate_amt(amt):
    """
    This function validates that the amount the user wants to pay should not be negative.
    """
    if amt < 0:
        raise ValueError("Please enter a valid amount")


def validate_uname(user, uname):
    """
    This function validates if the username entered by the user is the same as the one decoded from the JWT.
    """
    if user.username != uname:
        raise HTTPException(
            status_code=401, detail="The user has not entered the right credentials"
        )


def validate_balance(user_deposit_bal, amt_to_wthdrw):
    """
    This function validates that the user doesn't enter an amount for a payment that exceeds their wallet balance.
    """
    if user_deposit_bal < amt_to_wthdrw:
        raise ValueError("Not enough Balance")


def validate_userexists(res):
    """
    This function validates whether the username entered by the user exists in the database or not.
    """
    if len(res) == 0:
        raise HTTPException(
            status_code=404, detail="The user details could not be found."
        )
