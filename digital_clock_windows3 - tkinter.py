import datetime
import tkinter as tk
import os 

# Create the main window
window = tk.Tk()
window.title("Current Time")

# Create a label widget to display the time
# time_label = tk.Label(window, text="")
time_label = tk.Label(window, text="", font=("Calibry", 65))

# show the current time in format hh:mm:ss in first row, second row - date
current_time = datetime.datetime.now().strftime("%H:%M:%S %d.%m.%Y") 


# show day of week
current_time = datetime.datetime.now().strftime("%A")

# show number of week
current_time = datetime.datetime.now().strftime("%U")


# # show number of day from the beginning of the year
# current_time = datetime.datetime.now().strftime("%j")

# show if have any active  users in my local network and show their names
active_users = os.popen('net user').read()
# save active users in list
actives = [ line.split()[0] for line in active_users.splitlines() if line.strip() and not line.startswith('User') ]




# Set the label text to the current time
time_label.config(text=current_time)

# Pack the label widget into the window
time_label.pack()

# Define a function to update the label text every second
def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S" + "\n" + "%d.%m.%Y" + '\n' + '%U' + ' Week' + '\n' + '%A' + '\n' + '%j' + ' Day' + '\n' + ('\n'.join(actives)))
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Call the update_time function to start updating the label text
update_time()

# Run the main loop
window.mainloop()
