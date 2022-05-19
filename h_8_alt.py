# initialization
from calendar import month
from datetime import date, datetime, timedelta
from datetime import timedelta

B_D_list = {'Test1':'19.05.2017',
            'Test2':'19.05.2022',
            'TestFinal':'25.05.2015'}
days_name = {
    "Monday":[] ,
    "Tuesday":[],
    "Wednesday":[],
    "Thurthday":[],
    "Friday":[],
    "Saturday":[],
    "Sunday":[],
}

def get_birthdays_per_week(users):
#day manipulation

  run_day = datetime.now().date()
  if run_day.weekday() == 6:
        begin_day = -2
  elif run_day.weekday() == 5:
        begin_day = -1
  else:
        begin_day = 0
  print(run_day.weekday())      
  days_name_work = days_name
  days_name_work = {run_day + timedelta(days=i): [] for i in range(begin_day, begin_day + 7)}
  for names, birthday in users.items():
    bday = datetime.strptime(birthday, '%d.%m.%Y').date()
    for key, value in days_name_work.items():
        if bday.month == key.month and bday.day == key.day:
            value.append(names)
  for i in days_name.keys():
    if i == 'Saturday' or i == 'Sunday':
      i = 'Monday'
    string = ''+ i +': '
    for v in days_name_work.values():
      if v == []:
        continue
      string = string + str(v) +'\n'
      string = string.replace('[','').replace(']','').replace('\'','')
  print(string)

get_birthdays_per_week(B_D_list)
  
