import pandas as pd
from pathlib import Path
import os
import re

ROOT = Path.cwd()
DATA_DIR = ROOT / "datasets"
IPEDS_DIR = DATA_DIR / "ipeds"
IC_DIR = IPEDS_DIR / "institutional_characteristics"
COST1_DIR = IPEDS_DIR / "cost1"
PROCESSED_DIR = IPEDS_DIR / "processed"

# takes in a filename of an instutional characteristic or cost1 file and returns a dataframe containng the uc application fee indexed by the unitid
def get_appl_fee(file_name : str, inCost : bool) -> pd.DataFrame:

    year = re.search(r"[1,2]\d{3}", file_name)

    # years before 2000 sometimes just list the last 2 digits of the year
    if (year == None):
        year = re.search(r"\d{2}", file).group()
        year = "19" + year
    else:
        year = year.group()


    # check if the file is from cost1
    if (inCost):
        ic = pd.read_csv(COST1_DIR / file_name)
    else:
        # pre-2000 range data is not encoded utf-8
        ic = pd.read_csv(IC_DIR / file_name, encoding="cp1252")
    
    ic.columns = ic.columns.str.upper()
    ic = ic[["UNITID","APPLFEEU"]]

    ic.columns = ["UNITID", year]

    return ic



files = os.listdir(IC_DIR)

output = 0
for file in files:
    print(file)
    col = get_appl_fee(file, False)
    if (type(output) == int):
        output = col
        continue
    output = pd.merge(output, col, on="UNITID", how="outer")

# years 2024 and higher move application cost to the cost1 dataset
newfiles = os.listdir(COST1_DIR)
for file in newfiles:
    print(file)
    col = get_appl_fee(file, True)
    if (type(output) == int):
        output = col
        continue
    output = pd.merge(output, col, on="UNITID", how="outer")

output = output.fillna(0)
output = output[["UNITID"] + sorted(output.columns.drop("UNITID"), key=int)]
print(output)

output.to_csv(PROCESSED_DIR / "merged_application_fees.csv", index = False)