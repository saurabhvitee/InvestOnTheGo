import binascii
import os
import time
from typing import Dict

import jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from DAO import *
from models import UserInfo
from queries import *

JWT_SECRET = binascii.hexlify(os.urandom(24))
JWT_ALGORITHM = "HS256"


def token_response(token: str):
    """
    This function generates the token response when a token is created.
    """
    return {"access_token": token}


def signJWT(username: str) -> Dict[str, str]:
    """
    This function creates a JWT for a user.
    """
    payload = {"username": username, "expires": time.time() + 315360000}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    """
    This function decodes the JWT to give the user's username back.
    """
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


class UserInfoResolver(HTTPBearer):
    """
    This class allows for the JWT to be extracted from HTTPBearer.
    """

    def __init__(self, auto_error: bool = True):
        """
        This function is the constructor for UserInfoResolver.
        """
        super(UserInfoResolver, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        """
        This function extracts the credentials from the HTTP Request.
        """
        credentials: HTTPAuthorizationCredentials = await super(
            UserInfoResolver, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            payload = self.verify_jwt(credentials.credentials)
            if not payload:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            curr_uname = get_user_info(payload["username"])
            return curr_uname
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        """
        This function verifies if the decoded JWT exists or not.
        """
        decoded_token = decodeJWT(jwtoken)
        if not decoded_token:
            return None
        else:
            return decoded_token


def get_user_info(username):
    """
    This function gets the required information about the user once username has been extracted from JWT.
    """
    curr_user = UserInfoDao(username)
    rname = curr_user.get_name_of_user()[0][0]
    sender_mainwallet_id, sender_depositwallet_id = generate_wallet_names(username)

    user_info = UserInfo(
        username=username,
        sender_mainwallet_id=sender_mainwallet_id,
        rname=rname,
        sender_depositwallet_id=sender_depositwallet_id,
    )
    return user_info
