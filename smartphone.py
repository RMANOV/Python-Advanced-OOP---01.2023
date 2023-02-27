# Smartphone
# Create a class called Smartphone. Upon initialization, it should receive a memory (number). 
# It should also have 2 other instance attributes: apps (empty list by default) and is_on (False by default). 
# Create 3 methods:
# -	power() - sets is_on on True if the phone is off, otherwise sets it to False
# -	install(app, app_memory)
# o	If there is enough memory on the phone and it is on, 
# installs the app (add it to apps and decrease the memory of the phone) and returns "Installing {app}"
# o	If there is enough memory, but the phone is off, returns "Turn on your phone to install {app}"
# o	Otherwise, returns "Not enough memory to install {app}"
# -	status() - returns "Total apps: {total_apps_count}. Memory left: {memory_left}"


class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, app, app_memory):
        if self.memory >= app_memory and self.is_on:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"
        elif self.memory >= app_memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
