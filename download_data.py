import pandas as pd
from hydro_requests import request_hourly
from write_to_csv import save_to_csv
from read_csv import get_usage
import datetime as dt
import re

JSESSION_ID = '0000DPQDpc8s513fAxVGuKpivDU:1gupvju42'
FOLDER_NAME = 'name'

start_date = dt.date(2023, 3, 1)
end_date = dt.date(2024, 3, 12)

dates = [dt.date.strftime(end_date - dt.timedelta(days=i), '%Y-%m-%d') for i in range(0, (end_date - start_date).days + 1)]

for date in dates:
    response = request_hourly(JSESSION_ID, date)
    save_to_csv(response.text, folder_name=FOLDER_NAME)

dfs = []
for date in dates:
    dfs.append(get_usage(date))

pd.concat(dfs).to_csv('output.csv', index=False)