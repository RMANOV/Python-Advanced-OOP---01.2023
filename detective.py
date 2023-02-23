# Write a function that takes (from file) ip address, mac address, user text - device owner, first detected time and date, last detected time and date, detection count, active status - yes or no, and a list of all the devices that have been detected. 
# Function should return all the devices (user text - device owner) that have been detected to connect and disconect oftenly - mostly together.
# Inner list should contain the device owner, first detected time and date, last detected time and date, detection count and mac address and ip address.


def detective():
    
    def get_data():
        # get data from file
        with open('data.txt', 'r') as f:
            data = f.readlines()
            # create a list of lists - each list is a row from the file
            data = [i.split() for i in data]
            # create a list of dictionaries - each dictionary is a row from the file
            data = [dict(zip(['ip', 'mac', 'user', 'first', 'last', 'count', 'active'], i)) for i in data]
            # convert all the values to the right type
            for i in data:
                i['first'] = datetime.datetime.strptime(i['first'], "%d.%m.%Y %H:%M:%S")
                i['last'] = datetime.datetime.strptime(i['last'], "%d.%m.%Y %H:%M:%S")
                i['count'] = int(i['count'])
            return data
    
    # define a function that filters same day, same hour, minute + or - 7 minutes and all connected devices (from  mac address) in this time period.
    # if pair or more evices are connected and disconnected more than 3 times, add pair to a list
    # iterate through the current day, hour, minute - 5 minutes, minute + 5 minutes - and check if there are more than 3 detections
    # identify the devices by mac address only - if mac address is the same, it is the same device
    # for every date create a dictionary - with mac address as key and list of all the devices that have conect and disconnect with it
    def paired_devices(data):
        # create a dictionary with mac address as key and list of all the devices that have conect and disconnect with it
        paired_devices = {}
        # iterate through the data
        for i in data:
            # if mac address is not in the dictionary, add it
            if i['mac'] not in paired_devices:
                paired_devices[i['mac']] = []
            # iterate through the data again
            for j in data:
                # if mac address is not in the dictionary, add it
                if j['mac'] not in paired_devices:
                    paired_devices[j['mac']] = []
                # if mac address is not the same, and the devices are connected and disconnected in the same minute or minute + or - 7 minutes, add the user text - device owner to the list.
                if i['mac'] != j['mac'] and i['first'] == j['last'] and (i['first'] - datetime.timedelta(minutes=7) <= j['first'] <= i['first'] + datetime.timedelta(minutes=7)):
                    paired_devices[i['mac']].append(j['user'])
                    paired_devices[j['mac']].append(i['user'])
        return paired_devices
    
    
    # define a function that count how mani times - 
    # one device is connected and disconnected with another device 
    # and return a list of devices that are connected and disconnected more than 3 times together 
    # sorted by the number of times they are connected and disconnected together
    def count_together(paired_devices):
        # create a list of devices that are connected and disconnected more than 3 times together
        together = []
        # iterate through the dictionary
        for i in paired_devices:
            # create a dictionary with mac address as key and list of all the devices that have conect and disconnect with it
            together_dict = {}
            # iterate through the list of devices
            for j in paired_devices[i]:
                # if device is not in the dictionary, add it
                if j not in together_dict:
                    together_dict[j] = 0
                # count how many times the device is connected and disconnected with another device
                together_dict[j] += 1
            # iterate through the dictionary
            for j in together_dict:
                # if the device is connected and disconnected more than 3 times together, add it to the list
                if together_dict[j] > 3:
                    together.append(j)
        # sort the list by the number of times they are connected and disconnected together
        together = sorted(together, key=lambda x: together.count(x), reverse=True)
        return together
    
    
    # define a function that returns a list of devices that are connected and disconnected more than 3 times together with given from the console device
    def detective(data, together, user):