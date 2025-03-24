import datetime
from GOCI_url import GOCI_URL

if __name__ == "__main__":
    dt = datetime.datetime(2020, 1, 31)
    goci_url = GOCI_URL(datetime=dt)
