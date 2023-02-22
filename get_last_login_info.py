import os
import re
import datetime


def get_last_login():
    # Get the output of the "net user" command as a string
    net_user_output = os.popen("net user").read()
    # get word from 25 to 31 position
    username = net_user_output[21:27]

    # Find the current username - it's the first word after "\\\\" and before "\"
    # username_match = re.search(r"\\\\([a-zA-Z]+)\\", net_user_output)
    # if username_match:
    #     username = username_match.group(1)
    # else:
    #     print("Could not find username.")
    #     return None

    # Run the "net user" command for the current user to get the last login time
    net_user_output = os.popen(f"net user {username}").read()

    # Find the line with the last login time
    last_login_match = re.search(r"Last logon\s+(.+)", net_user_output)
    if last_login_match:
        last_login_str = last_login_match.group(1).strip()
    else:
        print("Could not find last login time.")
        return None

    # Convert the last login time string to a datetime object
    try:
        last_login = datetime.datetime.strptime(last_login_str, "%m/%d/%Y %I:%M:%S %p")
    except ValueError:
        print("Could not parse last login time.")
        return None

    return last_login


get_last_login()
