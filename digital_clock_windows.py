import datetime

# Get the current time
current_time = datetime.datetime.now().time()
# format the time - hh:mm:ss
print("Current time:", current_time.strftime("%H:%M:%S"))

# Get the current date
current_date = datetime.date.today()
# format the date - dd/mm/yyyy
print("Current date:", current_date.strftime("%d.%m.%Y"))