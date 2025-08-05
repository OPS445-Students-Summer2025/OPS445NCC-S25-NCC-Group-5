#!/usr/bin/env python3
"""
Author: Sultan Mahamud
"""

import os   #we are importing the os module so we can run  commands like 'uname', 'df', 'free' from Python using os.popen()



def get_system_info():  #function to gather general system information

    info = []  #this command will store all the system info messages in this info list and return it at the end
    hostname = os.popen('hostname').read().strip() #'hostname' command returns the name of the computer.we read and strip the newline character
    info.append("Hostname: " + hostname)    #adding hostname string to the list

#OS information
    os_info = os.popen('uname -o').read().strip()  #'uname -o' returns the operating system type
    info.append("Operating System: " + os_info)  #adding OS type to the list
#Kernel Version information
    kernel = os.popen('uname -r').read().strip() #'uname -r' gives the kernel version the OS is currently using
    info.append("Kernel Version: " + kernel)  #adding kernel version string to the list.

    uptime = os.popen('uptime -p').read().strip() #'uptime -p' returns system uptime in a more human readable format like "up 2 hours, 5 minutes"
    info.append("Uptime: " + uptime)  #adding uptime string to the list


    return info #it returns the info list so the calling function can print it or use it later

if __name__ == "__main__":
    system_info = get_system_info()
    
    print("\nSystem Information:")
    print("------------------")
    for item in system_info:
        print(item)
    print()
