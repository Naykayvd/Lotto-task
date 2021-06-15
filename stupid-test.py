import datetime
import rsaidnumber
from datetime import *

id = input("KOPPLE ID JY")
year = id[:2]
if year >= "22":
    year = "19" + year
else:
    year = "20" + year
month = id[2:4]
day = id[4:6]