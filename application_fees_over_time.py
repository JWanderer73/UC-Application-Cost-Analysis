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

# takes in a filename of an instutionalm characteristic or cost1 file and returns a dataframe containng the ug application fee indexed by the unitid
def get_appl_fee(file_name : str, inCost : bool) -> pd.DataFrame:

    year = re.search(r"\d{4}",file_name).group()

    # check if the file is from cost1
    if (inCost):
        ic = pd.read_csv(COST1_DIR / file_name)
    else:
        ic = pd.read_csv(IC_DIR / file_name)
    
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
print(output)

output.to_csv(PROCESSED_DIR / "merged_application_fees.csv", index = False)