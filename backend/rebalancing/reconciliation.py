from database import DatabaseConnectionManager
from query import *

cur = DatabaseConnectionManager.get_cursor()
status = ("completed", "processing")
cur.execute(RECONCILIATION_OF_TRANSACTION, status)
DatabaseConnectionManager.commit_transaction()
