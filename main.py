import datetime
from GOCI_url import GOCI_URL

if __name__ == "__main__":
    dt = datetime.datetime(2019, 8, 12)
    goci_url = GOCI_URL(datetime=dt)
    for url in goci_url.L1B_url:
        print(url)
