import datetime
import tkinter as tk
import os
import re

# Create the main window
window = tk.Tk()
window.title("Current Time")

# Create a label widget to fully fill the all window
time_label = tk.Label(
    window, text="", font=("Calibry", 65), bg="black", fg="white", bd=0
)


def get_last_restart():
    # this function should be called only once a day
    last_restart_date = ''
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    
    if last_restart_date != current_date:
        systeminfo = os.popen("systeminfo").read()
        match = re.search(r"System Boot Time:\s+(.+)", systeminfo)
        if match:
            try:
                last_restart_str = match.group(1)
                last_restart_date, junk, last_restart_time = last_restart_str.split(" ")
                last_restart = (last_restart_date + "-" + last_restart_time).strip()
                return last_restart_date, last_restart_time
            except ValueError:
                print("Could not get last restart time.")
                return None


# Define a function to update the label text every second
def update_time():
    # Format the current time and date as separate variables
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")

    # do not update the uptime every second - only once a day
    last_restart_date = ""
    if last_restart_date != current_date:
        last_r = get_last_restart()
        # last_l = get_last_login()
        last_restart_date = current_date
        current_week = datetime.datetime.now().strftime("%U Week")
        current_day = datetime.datetime.now().strftime("%A")
        current_year_day = datetime.datetime.now().strftime("%j Day")

    # calculate the uptime in days and hours
    uptime = f'{ (datetime.datetime.now() - datetime.datetime.strptime(last_r[0], "%d.%m.%Y")).days} days, { (datetime.datetime.now() - datetime.datetime.strptime(last_r[1], "%H:%M:%S")).seconds // 3600} hours'


    # Concatenate the date, time, and active users into a single string
    current_time_str = f"{current_time}\n{current_date}\n{current_week}\n{current_day}\n{current_year_day}\nUp-time: {uptime}\nUp-time date: {last_r[0]}\nUp-time time: {last_r[1]}"

    # Update the label text
    time_label.config(text=current_time_str)

    # Schedule the function to run again after 1 second
    window.after(1000, update_time)


# Call the update_time function to start updating the label text
update_time()

# Pack the label widget into the window
time_label.pack()

# Run the main loop
window.mainloop()
