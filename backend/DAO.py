import validations
from config import *
from database import DatabaseConnectionManager
from queries import *
from utils import *


class RegistrationDAO:
    """
    This class takes care of all queries required to register a new user.
    """

    def __init__(self, username):
        """
        The constructor for RegistrationDAO class

        Parameters:
            username (string): Username of the user
        """
        self.cursor = DatabaseConnectionManager.get_cursor()
        self.username = username

    def create_user(self, hashed_pwd, first_name, date_of_birth, phone_num):
        """
        The function to insert user information into database.

        Parameters:
            hashed_pwd (string): Hashed password of user.
            first_name (string): First name of user.
            date_of_birth (string): Date of birth of user.
            phone_num (string): Phone number of user.
        """

        loginDetailsTuple = (self.username, hashed_pwd)
        userDetailsTuple = (self.username, first_name, date_of_birth, phone_num)
        self.cursor.execute(INSERT_LOGIN_DETAILS, loginDetailsTuple)
        self.cursor.execute(INSERT_USER_DETAILS, userDetailsTuple)

    def create_user_wallet(self, main_wallet, deposit_wallet):
        """
        The function to insert user wallet information into database.

        Parameters:
            main_wallet (string): Main wallet of user.
            deposit_wallet (string): Deposit wallet of user.
        """
        walletDetailsTuple = (self.username, main_wallet, INIT_MAIN_AMT, "main")
        depositDetailsTuple = (self.username, deposit_wallet, INIT_DEP_AMT, "deposit")
        self.cursor.execute(INSERT_WALLET_DETAILS, walletDetailsTuple)
        self.cursor.execute(INSERT_WALLET_DETAILS, depositDetailsTuple)

    def create_investment_summary(self):
        """
        The function to insert the investment summary into database.
        """
        investmentDetailsTuple = (
            self.username,
            INIT_DEP_AMT,
            INIT_DEP_AMT,
            INIT_DEP_AMT,
        )
        self.cursor.execute(INSERT_INVESTMENT_SUMMARY, investmentDetailsTuple)

    def create_rewards(self):
        """
        The function to insert user rewards into database.
        """
        rewardDetailsTuple = (self.username, INIT_DEP_AMT)
        self.cursor.execute(INSERT_REWARD_DETAILS, rewardDetailsTuple)

    def create_returns(self):
        """
        The function to insert returns of user into database.
        """
        returnDetailsTuple = (self.username, INIT_DEP_AMT, INIT_DEP_AMT, INIT_DEP_AMT)
        self.cursor.execute(INSERT_RETURN_DETAILS, returnDetailsTuple)


class UserInfoDao:
    """
    This class takes care of getting user information from database.
    """

    def __init__(self, username):
        """
        The constructor for UserInfoDao class

        Paramters:
            username (string): Username of the user
        """
        self.cursor = DatabaseConnectionManager.get_cursor()
        self.username = username

    def get_login_details(self):
        """
        The function to fetch login details from database.
        """
        loginDetailsTuple = (self.username,)
        self.cursor.execute(GET_LOGIN_DETAILS, loginDetailsTuple)
        login_result = self.cursor.fetchall()

        validations.validate_userexists(login_result)

    def get_loginpwd_details(self, hashed_pwd):
        """
        The function to fetch login details with password as criteria from database.

        Parameters:
            hashed_pwd (string): Hashed password of user.
        """
        loginDetailsWithPasswordTuple = (self.username, hashed_pwd)
        self.cursor.execute(
            GET_LOGIN_DETAILS_WITH_PASSWORD, loginDetailsWithPasswordTuple
        )
        login_with_password_result = self.cursor.fetchall()
        validations.validate_userexists(login_with_password_result)

    def get_name_of_user(self):
        """
        The function to fetch user name from database.
        """
        nameTuple = (self.username,)
        self.cursor.execute(GET_NAME, nameTuple)
        name_result = self.cursor.fetchall()
        return name_result

    def get_wallet_amt(self, main_wallet, deposit_wallet):
        """
        The function to fetch wallet amount of user from database.

        Parameters:
            main_wallet (string): Main wallet of user.
            deposit_wallet (string): Deposit wallet of user.
        """
        mainAmountTuple = (main_wallet,)
        self.cursor.execute(GET_WALLET_AMOUNT, mainAmountTuple)
        main_amount_res = self.cursor.fetchall()
        depositAmountTuple = (deposit_wallet,)
        self.cursor.execute(GET_WALLET_AMOUNT, depositAmountTuple)
        deposit_amount_res = self.cursor.fetchall()
        return main_amount_res, deposit_amount_res


class WalletInfoDao:
    """
    This class takes care of wallet functionality for the user.
    """

    def __init__(self):
        """
        The constructor for WalletInfoDAO class
        """
        self.cursor = DatabaseConnectionManager.get_cursor()

    def update_wallet_amount(self, sender_bal, sender_mainwallet_id):
        """
        The function to update wallet amount according to payment.

        Parameters:
            sender_bal (string): Balance of sender.
            sender_mainwallet_id (string): Main wallet ID of sender.
        """
        main_amount_update_tuple = (str(sender_bal), sender_mainwallet_id)
        self.cursor.execute(UPDATE_WALLET_AMOUNT, main_amount_update_tuple)


class TransactionInfoDao:
    """
    This class takes care of the transactions made by a user.
    """

    def __init__(self, username):
        """
        The constructor for TransactionInfoDAO class

        Paramters:
            username (string): Username of the user
        """
        self.cursor = DatabaseConnectionManager.get_cursor()
        self.username = username
        # check init class is username needed?

    def fetch_transaction_details(self):
        """
        The function to fetch user transaction details.
        """
        main_wallet_id, deposit_wallet_id = generate_wallet_names(self.username)
        transactionDetailTuple = (main_wallet_id, deposit_wallet_id)
        self.cursor.execute(GET_USER_TRANSACTION_DETAILS, transactionDetailTuple)
        transaction_details = self.cursor.fetchall()
        return transaction_details

    def insert_transactiondetails_nostatus(
        self, paymentID, wallet_id, amount, transaction_type
    ):
        """
        The function to insert the transaction details with 'completed' status into database

        Parameters:
            paymentID (string): Payment ID of user.
            wallet_id (string): Wallet oID f user (can be either main or deposit).
            amount (string): Amount of user wallet.
            transaction_type (string): Transaction type of user.
        """
        insert_transaction_tuple = (paymentID, wallet_id, amount, transaction_type)
        self.cursor.execute(
            INSERT_TRANSACTION_DETAILS_NO_STATUS, insert_transaction_tuple
        )

    def insert_transactiondetails_with_status(
        self, paymentID, main_wallet_id, amt_to_wthdrw, transaction_type
    ):
        """
        The function to insert the transaction details with custom status into database

        Parameters:
            paymentID (string): Payment ID of user.
            main_wallet_id (string): Wallet oID f user (can be either main or deposit).
            amt_to_wthdrw (string): Amount to withdraw of user wallet.
            transaction_type (string): Transaction type of user.
        """
        insert_transaction_tuple = (
            str(paymentID),
            main_wallet_id,
            amt_to_wthdrw,
            transaction_type,
            PAYMENT_STATUS,
        )
        self.cursor.execute(
            INSERT_TRANSACTION_DETAILS_WITH_STATUS, insert_transaction_tuple
        )


class PaymentInfoDao:
    """
    This class takes care of payment details of a user.
    """

    def __init__(self, username):
        """
        The constructor for PaymentInfoDAO class

        Paramters:
            username (string): Username of the user
        """
        self.cursor = DatabaseConnectionManager.get_cursor()
        self.username = username
        # can init be updated to make other functions easier

    def get_payment_id(self, sender_mainwallet_id, receiver_mainwallet_id, amt_to_pay):
        """
        The function to get payment ID of a particular payment.

        Parameters:
            sender_mainwallet_id (int): The sender's main wallet id..
            receiver_mainwallet_id (int): The receiver's main wallet id.
            amt_to_pay (int): Amount paid during payment

        Returns:
            query_result: the payment ID of the particular payment.
        """
        fetch_pay_id_tuple = (sender_mainwallet_id, receiver_mainwallet_id, amt_to_pay)
        self.cursor.execute(FETCH_PAYMENT_ID, fetch_pay_id_tuple)
        query_result = self.cursor.fetchall()
        return query_result

    def inserting_payment_details_nostatus(
        self, sender_mainwallet_id, receiver_mainwallet_id, amt_to_pay
    ):
        """
        The function to insert payment details of a particular payment with 'completed' status.

        Parameters:
            sender_mainwallet_id (string): The sender's main wallet id..
            receiver_mainwallet_id (string): The receiver's main wallet id.
            amt_to_pay (int): Amount paid during payment
        """
        payment_details_insertion_tuple = (
            sender_mainwallet_id,
            receiver_mainwallet_id,
            str(amt_to_pay),
        )
        self.cursor.execute(
            INSERTION_OF_PAYMENT_DETAILS_NO_STATUS, payment_details_insertion_tuple
        )

    def inserting_payment_details_with_status(
        self, deposit_wallet_id, main_wallet_id, amt_to_wthdrw
    ):
        """
        The function to insert payment details of a particular payment with custom status.

        Parameters:
            deposit_wallet_id (string): The deposit wallet id..
            main_wallet_id (int): The main wallet id.
            amt_to_wthdrw (string): Amount paid during withdrawal
        """
        payment_details_tuple = (
            deposit_wallet_id,
            main_wallet_id,
            amt_to_wthdrw,
            PAYMENT_STATUS,
        )
        self.cursor.execute(INSERT_PAYMENT_DETAILS_WITH_STATUS, payment_details_tuple)


class QuestionInfoDao:
    """
    This class handles the questionnaire responses filled by the user.
    """

    def __init__(self, username):
        """
        The constructor for QuestionInfoDAO class

        Paramters:
            username (string): Username of the user
        """
        self.cursor = DatabaseConnectionManager.get_cursor()
        self.username = username

    def insert_questions_responses(
        self,
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
    ):
        """
        The function to insert questionnaire responses into database.

        Parameters:
            question_one_response (int): q1 score
            question_two_response (int): q2 score
            question_three_response (int): q3 score
            question_four_response (int): q4 score
            question_five_response (int): q5 score
            question_six_response (int): q6 score
            question_seven_response (int): q7 score
            question_eight_response (int): q8 score
            question_nine_response (int): q9 score
            question_ten_strings (string): q8 list of sector
            question_eleven_strings (string): q9 list of cap
        """
        questionResponsesTuple = (
            self.username,
            int(question_one_response),
            int(question_two_response),
            int(question_three_response),
            int(question_four_response),
            int(question_five_response),
            int(question_six_response),
            int(question_seven_response),
            int(question_eight_response),
            int(question_nine_response),
            question_ten_strings,
            question_eleven_strings,
        )
        self.cursor.execute(INSERT_QUESTION_RESPONSES, questionResponsesTuple)


class PositionInfoDao:
    """
    This class is responsible for position information of a database.
    """

    def __init__(self, username):
        """
        The constructor for PositionInfoDao class.

        Paramters:
            username (string): Username of the user
        """
        self.cursor = DatabaseConnectionManager.get_cursor()
        self.username = username

    def insert_position_info(self):
        """
        The function to fetch position information from database.

        Returns:
            positionInfoOfUser: the position information of user.
        """
        positionInfoTuple = (self.username,)
        self.cursor.execute(POSITION_INFORMATION, positionInfoTuple)
        positionInfoOfUser = self.cursor.fetchall()
        return positionInfoOfUser


class ReturnsInfoDao:
    """
    This function is responsible for Returns Information of a user.
    """

    def __init__(self, username):
        """
        The constructor for ReturnsInfoDAO class

        Paramters:
            username (string): Username of the user
        """
        self.cursor = DatabaseConnectionManager.get_cursor()
        self.username = username

    def get_returns_info(self):
        """
        The function to fetch returns information from the database

        Returns:
            returnInfoOfUser: Returns info of user.
        """
        returnInformationTuple = (self.username,)
        self.cursor.execute(RETURN_INFORMATION, returnInformationTuple)
        returnInfoOfUser = self.cursor.fetchall()
        return returnInfoOfUser
