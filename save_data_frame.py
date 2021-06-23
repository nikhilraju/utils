from datetime import date
date_today = str(date.today())
df.to_csv(f'../data/{date_today}')
