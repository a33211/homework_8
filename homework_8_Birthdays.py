from calendar import month
from datetime import date, datetime, timedelta

B_D_list = {'Test1':'19.05.2017',
            'Test2':'19.05.2022',
            'TestFinal':'25.05.2015'}
days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thurthday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
testing = {key: value[:-5] for (key, value) in B_D_list.items()}
print(testing)
# initialization

def get_birthdays_per_week(users):
  INTERVAL = timedelta(days=7)
  days_now_init = datetime.now()
  days_now = datetime.now() - timedelta(days_now_init.weekday()) # Week starts from 1 day
# !!!! ПРОБЛЕМЫ   days_now некорректно считает дни
# Дни рождения берутся почему-то с учетом года рождения. Почему так = хз
  finish_day = days_now + INTERVAL
  final = {}
  strings = []
  #worklist = {key: value[:-5] for (key, value) in B_D_list.items()}
  #print(f'worklist!!!! {worklist}') 
  #worklist = {
  #  key: datetime.strptime(value, "%d.%m.%Y").replace(year=2022) for (key, value) in B_D_list.items()
  #}
# Швидше за все, коли створюється key: datetime.strptime(value, "%d.%m.%Y") треба позбутись року
  #print(worklist) 


  for k, values in B_D_list.items():
    if datetime.strptime(values,"%d.%m.%Y").month == finish_day.month:
        if datetime.strptime(values,"%d.%m.%Y").day >= days_now.day and datetime.strptime(values,"%d.%m.%Y").day <= finish_day.day:
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

get_birthdays_per_week (B_D_list)




#B_D_list = {'Halyna':'17.10.1987',
  #          'Alex':'26.02.1986',
  #          'Nadiya':'09.09.1986',
  #          'Slava':'16.10.1978',
  #          'Alexey':'29.03.1976',
  #          'Test1':'15.05.2022',
  #          'Test2':'16.05.2022',
  #          'TestFinal':'19.05.2015'}