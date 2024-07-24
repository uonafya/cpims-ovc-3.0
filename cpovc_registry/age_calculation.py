from datetime import datetime, date
fmt = "%Y-%m-%d"

today = date.today()
todate = '2024-07-01'
today = datetime.strptime(todate, fmt)

date_of_birth = '2019-08-24'


dob = datetime.strptime(date_of_birth, fmt)
date_check = (today.month, today.day) < (dob.month, dob.day)
yrs = today.year - dob.year - date_check


print(date_check, yrs)