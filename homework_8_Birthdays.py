from calendar import month
from datetime import date, datetime, timedelta

B_D_list = {'Halyna':'17.10.1987',
            'Alex':'26.02.1986',
            'Nadiya':'09.09.1986',
            'Slava':'16.10.1978',
            'Alexey':'29.03.1976',
            'Test1':'15.05.2022',
            'Test2':'16.05.2022',
            'Test3':'16.05.2022'}
days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thurthday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
def get_birthdays_per_week(users):
  INTERVAL = timedelta(days=7)
  days_now_init = datetime.now()
  days_now = datetime.now() - timedelta(days_now_init.weekday()) # Week starts from 1 day
  finish_day = days_now + INTERVAL
  final = {}
  strings = []
  worklist = {  
    key: datetime.strptime(value, "%d.%m.%Y") for (key, value) in B_D_list.items()
}
  for k, values in worklist.items():
    if values.month == finish_day.month:
        if values.day >= days_now.day and values.day <= finish_day.day:
            values = days_name.get(values.weekday())
            if values in ["Saturday", "Sunday"]:
                values = "Monday"
            if final.get(values):
                final[values].append(k)
            else:
                final[values] = [k]
  for key,item in final.items():
    strings.append("{}: {}".format(key.capitalize(), item))
  result = "\n".join(strings)
  result = result.replace('[','').replace(']','').replace('\'','')
  return print(result)

if __name__ == __main__:

  get_birthdays_per_week (B_D_list)




