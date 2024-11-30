import logging
import pprint

import mysql.connector as MSQC
import pandas as pd

from database import DatabaseConnectionManager
from query import *
from workflow_configuration import RISK_WEIGHTS

cur = DatabaseConnectionManager.get_cursor()

cur.execute(GET_FUNDS)
funds_data_to_df = pd.DataFrame(
    cur.fetchall(),
    columns=[
        "etfsymbol",
        "Leveraged",
        "Asset_Class_Size",
        "Price",
        "General_Sector",
        "Specific_Sector",
        "beta",
        "standard_deviation",
        "20_Day_MA",
        "60_Day_MA",
        "Volatility",
        "1_Month_Return",
        "5_Year_Return",
    ],
)
funds_data_to_df_dict = funds_data_to_df[
    [
        "etfsymbol",
        "Leveraged",
        "Asset_Class_Size",
        "Price",
        "General_Sector",
        "Specific_Sector",
        "beta",
        "standard_deviation",
        "20_Day_MA",
        "60_Day_MA",
        "Volatility",
        "1_Month_Return",
        "5_Year_Return",
    ]
].copy()

funds_raw_data = funds_data_to_df_dict.to_dict("records")
funds_processed_data = {}


def weighted_average(nums, weights):
    """
    This function calculates the weighted average of the parameters we're using for risk analysis.

    Parameter:
        nums: The parameters we want to calculate the weighted average of.
        weights: The weights we want to assign to the parameters.
    """
    return sum(x * y for x, y in zip(nums, weights)) / sum(weights)


def normalisation(property, range_max=float("-inf"), range_min=float("inf")):
    """
    This function normalises all the parameters used for analysis.

    Parameter:
        property: The parameter we want to normalise.
        range_max: Max value ot the parameter.
        range_min: Min value of the parameter.
    """
    for fund in funds_raw_data:
        value = fund[property]
        if property == "standard_deviation" or property == "Volatility":
            value = value[:-1]

        try:
            range_max = max(range_max, float(value))
            range_min = min(range_min, float(value))
        except ValueError:
            continue
    diff = range_max - range_min
    for fund in funds_raw_data:
        value = fund[property]
        if property == "standard_deviation" or property == "Volatility":
            value = value[:-1]

        try:
            temp = ((float(value) - range_min) * 10) / diff
        except:
            temp = 0

        try:
            funds_processed_data[fund["etfsymbol"]][property] = str(temp)
        except KeyError:
            funds_processed_data[fund["etfsymbol"]] = {}
            funds_processed_data[fund["etfsymbol"]][property] = temp

        del temp

    logging.info("all parameters were successfully normalised")


for fund in funds_raw_data:

    moving_average_60days = (fund["60_Day_MA"])[1:]
    moving_average_20days = (fund["20_Day_MA"])[1:]
    Return_5_yr = (fund["5_Year_Return"])[:-1]
    Return_1_month = (fund["1_Month_Return"])[:-1]
    try:
        fund["diff in MA"] = str(
            float(moving_average_60days) - float(moving_average_20days)
        )
    except ValueError:
        fund["diff in MA"] = 5
    try:
        fund["term score"] = str(float(Return_5_yr) - float(Return_1_month))
    except ValueError:
        fund["term score"] = 5

normalisation("beta")
normalisation("standard_deviation")
normalisation("Volatility")
normalisation("Leveraged")
normalisation("diff in MA")
normalisation("term score")
normalisation("Price")

for fund in funds_processed_data:
    parameters = [
        float(funds_processed_data[fund]["beta"]),
        float(funds_processed_data[fund]["standard_deviation"]),
        float(funds_processed_data[fund]["Volatility"]),
        float(funds_processed_data[fund]["Leveraged"]),
        float(funds_processed_data[fund]["diff in MA"]),
    ]
    risk_weights = RISK_WEIGHTS
    weighted_mean = weighted_average(parameters, risk_weights)
    funds_processed_data[fund]["risk score"] = weighted_mean


for fund in funds_raw_data:
    funds_processed_data[fund["etfsymbol"]]["Specific_Sector"] = fund["Specific_Sector"]
    if fund["Asset_Class_Size"] == "Small-Cap":
        funds_processed_data[fund["etfsymbol"]]["Asset_Class_Size"] = 0
    if fund["Asset_Class_Size"] == "Large-Cap":
        funds_processed_data[fund["etfsymbol"]]["Asset_Class_Size"] = 10
    if fund["Asset_Class_Size"] == "Multi-Cap":
        funds_processed_data[fund["etfsymbol"]]["Asset_Class_Size"] = 5
    if fund["Asset_Class_Size"] == "Mid-Cap":
        funds_processed_data[fund["etfsymbol"]]["Asset_Class_Size"] = 5
    if fund["Asset_Class_Size"] == "Micro-Cap":
        funds_processed_data[fund["etfsymbol"]]["Asset_Class_Size"] = 0
    if fund["Asset_Class_Size"] == "None":
        funds_processed_data[fund["etfsymbol"]]["Asset_Class_Size"] = 5
    if fund["Asset_Class_Size"] == "Mega-Cap":
        funds_processed_data[fund["etfsymbol"]]["Asset_Class_Size"] = 10
    logging.info("funds were successfully mapped to cap")

funds_final_data = {}
for fund in funds_processed_data:
    try:
        funds_final_data[fund]["term score"] = funds_processed_data[fund]["term score"]
        funds_final_data[fund]["risk score"] = funds_processed_data[fund]["risk score"]
        funds_final_data[fund]["Price"] = funds_processed_data[fund]["Price"]
        funds_final_data[fund]["Asset_Class_Size"] = funds_processed_data[fund][
            "Asset_Class_Size"
        ]
        funds_final_data[fund]["Specific_Sector"] = funds_processed_data[fund][
            "Specific_Sector"
        ]
        logging.info("final fund data successfully calculated")
    except KeyError:
        funds_final_data[fund] = {}
        funds_final_data[fund]["term score"] = funds_processed_data[fund]["term score"]
        funds_final_data[fund]["risk score"] = funds_processed_data[fund]["risk score"]
        funds_final_data[fund]["Price"] = funds_processed_data[fund]["Price"]
        funds_final_data[fund]["Asset_Class_Size"] = funds_processed_data[fund][
            "Asset_Class_Size"
        ]
        funds_final_data[fund]["Specific_Sector"] = funds_processed_data[fund][
            "Specific_Sector"
        ]

pprint.pprint(funds_final_data)
del funds_raw_data

shortlisted_funds = funds_final_data.keys()
cur.execute(DEL_FUND_SCORE)
for fund in shortlisted_funds:
    fundname = fund
    risk_score = funds_final_data[fund]["risk score"]
    term_score = funds_final_data[fund]["term score"]
    dept_score = funds_final_data[fund]["Price"]
    Asset_Class_Size = funds_final_data[fund]["Asset_Class_Size"]
    Specific_Sector = funds_final_data[fund]["Specific_Sector"]

    try:
        val = (
            fundname,
            risk_score,
            term_score,
            dept_score,
            Asset_Class_Size,
            Specific_Sector,
        )
        cur.execute(INSERT_INTO_FUND_SCORE, val)
        logging.info("fund scores were successfully inserted")
    except Exception as e:
        logging.error(
            "Error in inserting funds_raw_data into fund_score table", exc_info=True
        )

DatabaseConnectionManager.commit_transaction()
logging.info(
    "fund scores were successfully calculated and inserted in fund_score table"
)
