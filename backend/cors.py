from fastapi.middleware.cors import CORSMiddleware

origins = {
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:8000/v1/register",
    "http://127.0.0.1:8000/v1/login",
    "http://127.0.0.1:8000/v1/check/wallet/balance",
    "http://127.0.0.1:8000/v1/question",
    "http://127.0.0.1:8000/v1/dashboard/wallet",
    "http://127.0.0.1:8000/v1/dashboard/wallet/withdraw",
    "http://127.0.0.1:8000/v1/history/{uname}",
    "http://127.0.0.1:8000/v1/returns/profit/{uname}",
    "http://127.0.0.1:8000/v1/returns/allocation/{uname}",
    "http://localhost:5173/signin",
    "http://localhost:5173/signup",
    "http://localhost:5173/question",
    "http://localhost:5173/dashboard",
    "http://localhost:5173/history/{uname}",
    "http://localhost:5173/returns",
    "http://localhost:5173",
    # list more origins
}


def enable_cors_for_react_ui(app):
    """
    This function allows to enable cross origin requests for frontend.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
