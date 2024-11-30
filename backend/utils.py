def generate_wallet_names(username):
    """
    This function generates a user's main wallet ID and deposit wallet ID.
    """
    id = ""
    id = username.split("@")[0]
    wallet1_id = id + ".main"
    wallet2_id = id + ".deposit"
    return [wallet1_id, wallet2_id]
