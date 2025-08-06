#!/usr/bin/env python3

import os #this line imports the os module from the python library.

def get_cpu_info(): #Here we are defining a function to get cpu info. 
    info = [] #This makes an empty list to store the data which our code will give.
    cpu_model = os.popen("grep 'model name' /proc/cpuinfo | head -1").read().strip() #This runs a shell command to get the information about CPU model name, which does not count space and it only extracts the values after ':'
    info.append("CPU Model: " + cpu_model) #This adds the CPU model to the info list which we created. 

    cpu_cores = os.popen("grep -c processor /proc/cpuinfo").read().strip() #This is the shell command to get the number of CPU cores or threads exists. 
    info.append("CPU Cores: " + cpu_cores) #This line adds the number of Cores or threads to the info list.

    return info #This line returns the info list with the CPU Model and Cores or Threads count.

if __name__ == "__main__":
    cpu_info = get_cpu_info() #This calls the function to get the CPU information.
    for line in cpu_info: #This line loops through all the lines in the info list.
        print(line) #This line prints the CPU Information line by line.
