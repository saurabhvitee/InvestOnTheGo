from typing import List

from pydantic import BaseModel


class LoginItem(BaseModel):
    """
    This class is defined to reflect the login details
    entered by the user.
    """

    username: str
    password: str


class RegisterItem(BaseModel):
    """
    This class is defined to reflect the registration details
    enetered by the user.
    """

    username: str
    password: str
    first_name: str
    last_name: str
    phone_no: str
    DOB: str


class WalletItem(BaseModel):
    """
    This class is defined to reflect the wallet details when
    a user wants to make a transaction.
    """

    username: str  # extract from token
    sender_id: str
    receiver_id: str
    amount: float
    vals: dict


class DepositWithdrawItem(BaseModel):
    """
    This class is defined to reflect thedetails of withdrawl
    from deposit wallet.
    """

    username: str
    amount: float


class UserInfo(BaseModel):
    """
    This class is defined to validate user's information once
    the JWT is decoded.
    """

    username: str
    sender_mainwallet_id: str
    sender_depositwallet_id: str
    rname: str


class QuestionItem(BaseModel):
    """
    This class is defined to store a user's questionnaire responses.
    """

    username: str
    q1: int
    q2: int
    q3: int
    q4: int
    q5: int
    q6: int
    q7: int
    q8: int
    q9: int
    q10: List[str]
    q11: List[str]
