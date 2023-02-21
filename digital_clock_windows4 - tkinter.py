import datetime
import tkinter as tk
import os

# Create the main window
window = tk.Tk()
window.title("Current Time")

# Create a label widget to fully fill the all window
time_label = tk.Label(window, text="", font=("Calibry", 65), bg="black", fg="white", bd=0)

# Define a function to get the active user names
def get_active_users():
    active_users = os.popen('net user').read()
    actives = [line.split()[0] for line in active_users.splitlines() if line.strip() and not line.startswith('User')]
    return actives

# Define a function to get the time from last restart
def get_last_restart():
    systeminfo = os.popen('systeminfo').read()
    for line in systeminfo.splitlines():
        if "System Boot Time" in line:
            try:
                last_restart_str = line.split(":")[1].strip()[:10]
                last_restart = datetime.datetime.strptime(last_restart_str,"%d.%m.%Y")
                return last_restart
            except ValueError:
                print("Could not get last restart time.")
                return None

# Define a function to get the time from last login
def get_last_login():
    lastlogontime = os.popen('net user %username%').read()
    for line in lastlogontime.splitlines():
        if "Last logon" in line:
            try:
                last_login_str = line.split(":")[1].strip()
                last_login = datetime.datetime.strptime(last_login_str, "%H:%M:%S, %d.%m.%Y")
                return last_login
            except ValueError:
                print("Could not get last login time.")
                return None

# Define a function to update the label text every second
def update_time():
    # Format the current time and date as separate variables
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    current_week = datetime.datetime.now().strftime("%U Week")
    current_day = datetime.datetime.now().strftime("%A")
    current_year_day = datetime.datetime.now().strftime("%j Day")
    
    # Try to get the last restart and login times
    try:
        uptime = str(datetime.datetime.now() - get_last_restart())
        last_login = str(datetime.datetime.now() - get_last_login())
    except TypeError:
        # If either value is None, set them to "unknown"
        uptime = "Unknown"
        last_login = "Unknown"
    
    # Get the list of active users
    actives = get_active_users()
    
    # Concatenate the date, time, and active users into a single string
    current_time_str = f"{current_time}\n{current_date}\n{current_week}\n{current_day}\n{current_year_day}\nLast login: {last_login}\nUp-time: {uptime}"
    
    # if actives - show them in small font
    if actives:
        current_time_str += "\n" + "\n".join(actives)
    
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
