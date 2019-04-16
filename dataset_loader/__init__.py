from dataset_manager import DatasetManager
import pandas as pd
import zipfile
import urllib.request
import os

PD_READ_FUNC = {
            "csv"   :   pd.read_csv,
            "xls"   :   pd.read_excel,
            "excel" :   pd.read_excel,
            "json"  :   pd.read_json
        }