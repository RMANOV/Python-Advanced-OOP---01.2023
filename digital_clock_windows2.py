import datetime
import kiwi

# Create the main window
window = kiwi.Window(title="Current Time")

# Create a label widget to display the time
time_label = kiwi.Label(window, text="")

# Format the current time as a string
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Set the label text to the current time
time_label.text = current_time

# Run the main loop
kiwi.run()

