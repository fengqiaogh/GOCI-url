import pandas as pd
from datetime import datetime


class GOCI_URL:
    def __init__(self, datetime: datetime):
        self.KOSC_L1_path = "https://kosc.kiost.ac.kr/download/downService.do?fileName=/home/goci/nfsdb/COMS/GOCI/L1/"

        self.datetime = datetime
        self.hour = []
        self.minute = []
        self.second = []
        self.get_HMS()

        self.L1B_filename = []
        self.get_L1B_filename()

        self.L1B_url = []
        self.get_L1B_url()

        # Ture color image
        self.TC = []
        self.get_ture_color_image()

        self.TSS = []
        self.L2C = []
        self.CHL = []
        self.RRS = []
        self.CDOM = []
        self.get_L2()

    def get_L2(self):
        base_url = "https://kosc.kiost.ac.kr/download/downService.do?fileName=/home/goci/nfsdb/COMS/GOCI/L2"

        L2A_base_date = f"COMS_GOCI_L2A_GA_{self.datetime.year}{self.datetime.month:>02d}{self.datetime.day:>02d}"
        L2C_base_date = f"COMS_GOCI_L2C_GA_{self.datetime.year}{self.datetime.month:>02d}{self.datetime.day:>02d}"
        file_path = f"{base_url}/{self.datetime.year}/{self.datetime.month:>02d}/{self.datetime.day:>02d}/L2/"
        for h, m, s in zip(self.hour, self.minute, self.second):
            base_time = f"{h}{m}{s}"
            TSS_name = f"{L2A_base_date}{base_time}.TSS.he5.zip"
            CDOM_name = f"{L2A_base_date}{base_time}.CDOM.he5.zip"
            CHL_name = f"{L2A_base_date}{base_time}.CHL.he5.zip"
            RRS_name = f"{L2A_base_date}{base_time}.RRS.he5.zip"
            L2C_name = f"{L2C_base_date}{base_time}.he5.zip"

            self.TSS.append(f"{file_path}{TSS_name}")
            self.CDOM.append(f"{file_path}{CDOM_name}")
            self.CHL.append(f"{file_path}{CHL_name}")
            self.RRS.append(f"{file_path}{RRS_name}")
            self.L2C.append(f"{file_path}{L2C_name}")

    def get_L1B_url(self):
        for filename in self.L1B_filename:
            self.L1B_url.append(
                f"{self.KOSC_L1_path}/{self.datetime.year}/{self.datetime.month}/{self.datetime.day}/L1B/{filename}.zip"
            )

    def get_L1B_filename(self):
        for h, m, s in zip(self.hour, self.minute, self.second):
            self.L1B_filename.append(
                f"COMS_GOCI_L1B_GA_{self.datetime.year}{self.datetime.month:>02d}{self.datetime.day:>02d}{h}{m}{s}.he5"
            )

    def get_HMS(self):
        df = pd.read_csv("datetime.csv")
        df = df.query(
            f"year=={self.datetime.year} & month=={self.datetime.month} & day=={self.datetime.day}"
        )

        for h, m, s in zip(df["hour"].values, df["minute"].values, df["second"].values):
            self.hour.append(f"{h:>02d}")
            self.minute.append(f"{m:>02d}")
            self.second.append(f"{s:>02d}")

    def get_ture_color_image(self):
        base_url = "https://oceancolor.gsfc.nasa.gov/cgi/gocibrs/"
        self.TC.append(f"{base_url}/{self.L1B_filename}_BRS.png")
