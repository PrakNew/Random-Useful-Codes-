import pytz
import datetime

abc= list(pytz.country_timezones)
abc1=list(pytz.all_timezones_set)
#print("-------------------------------------------------------------------")
#print(dir(pytz))

time_now_zone = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")
print(time_now_zone)
time ={}

for x in abc1:
    time[x]=datetime.datetime.now(pytz.timezone(x))
print(time['Asia/Kolkata'].strftime("%Y-%m-%d %H:%M:%S"))


time1= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for x in time:
    if time[x].strftime("%Y-%m-%d %H:%M:%S") == time1:
        print(x)
print('done')

# converting a string to a datetime object
date_object = datetime.strptime(date_string, "%d %B, %Y")

#converting a timezone to another timezone in python

my_timestamp = datetime.datetime.now()

old_tiimezone = pytz.timezone('UTC')
new_timezone = pytz.timezone('EST')

new_timezone_timestamp = old_timezone.localize(my_timestamp).astimezone(new_timezone)
print(new_timezone_timestamp.strftime('%Y-%m-%d %H:%M:%S'))