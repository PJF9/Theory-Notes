import datetime
import pytz

""" Datetime.date """

# Get an inputed date
d = datetime.date(2020, 1, 9)
print(d)

# Get todays day
today_date = datetime.date.today()
print(today_date)

# Get specific data from the date
print(today_date.year)

# Getting the day ( Monday, Tuesday, ... )
print(today_date.weekday()) # Monday = 0
print(today_date.isoweekday()) # Monday = 1

# Working with more time deltas
time_delta = datetime.timedelta(days=10) # Working with 10 days
print(today_date + time_delta) # Get the date 10 days in advaced ( We can aslo - )

# day2 = day1 [+ or (-)] timedelta
# timedelta = day1 [+ or (-)] day2

bday_date = today_date - d # In how many days
print(bday_date.days)
print(bday_date.total_seconds())


""" Datetime.time """

print()
t = datetime.time(9, 20, 50, 100000) # hours, minutes, seconds, microseconds
print(t)
print(t.hour)

# Combine both the .time and .date we can use .datetime
adv_date = datetime.datetime(2020, 6, 4, 12, 7, 30, 100) # year, month, day, hours, minutes, seconds, microseconds
print(adv_date)
print(adv_date.date()) # We can also grabe individual atributes ( .year )
print(adv_date.time())

# We can also work with timedeltas
time_delta_2 = datetime.timedelta(days=7)
time_delta_2 = datetime.timedelta(hours=12)
print(adv_date + time_delta_2)

# Today date
today_date_today = datetime.datetime.today() # The first 2 in the same with the difference that in .now we can add timezone option
today_date_now = datetime.datetime.now()
today_date_utcnow = datetime.datetime.utcnow()

print(today_date_today)
print(today_date_now)
print(today_date_utcnow) 


""" Timezone datetimes """

print()
new_date = datetime.datetime(2020, 6, 4, 12, 20, 30, 10000, tzinfo=pytz.UTC)
print(new_date)

# Get the current utc time
today_date_now = datetime.datetime.now(tz=pytz.UTC)
today_date_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(today_date_now)
print(today_date_utcnow)

# The bect way is the first
current_utc_date = datetime.datetime.now(tz=pytz.UTC)
# Convert into a different time zone
d = current_utc_date.astimezone(pytz.timezone("Europe/Athens"))
print(d)

# Printing all the timezones
for tz in pytz.all_timezones:
    if tz.startswith("Eu"):
        print(tz)

# Printing the datetime
current_date = datetime.datetime.now(tz=pytz.UTC)
current_date_time = current_date.astimezone(pytz.timezone("Europe/Athens"))

print(current_date_time.strftime("%d/%B/%Y"))

# Convert a string into a datetime
date_string = "04/June/2020"
dt = datetime.datetime.strptime(date_string, "%d/%B/%Y")
print(dt)

# strftime --> Convert a datetime into a string
# strptime --> Convert a string into a datetime