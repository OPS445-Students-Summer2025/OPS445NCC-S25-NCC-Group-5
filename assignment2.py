#!/usr/bin/env python3

import os #this line imports the os module from the python library.

def get_logged_in_users(): #this function checks who is currently logged into the system 
    users = [] #creating an empty list to hold our output lines

    output = os.popen('who').readlines() #running the who command to get logged in user  and read its lines

    for line in output: #loop through each line from the 'who' command output
        parts = line.split() #spliting the line into words to isolate the username 
        if len(parts) >= 1:
            username = parts[0]
            users.append("Currently logged in user: " + username)  #adding the username

    return users  #returns the list of user info lines


def get_cpu_info(): #Here we are defining a function to get cpu info. 
    info = [] #This makes an empty list to store the data which our code will give.
    cpu_model = os.popen("grep 'model name' /proc/cpuinfo | head -1").read().strip() #This runs a shell command to get the information about CPU model name, which does not count space and it only extracts the values after ':'
    info.append("CPU Model: " + cpu_model) #This adds the CPU model to the info list which we created. 

    cpu_cores = os.popen("grep -c processor /proc/cpuinfo").read().strip() #This is the shell command to get the number of CPU cores or threads exists. 
    info.append("CPU Cores: " + cpu_cores) #This line adds the number of Cores or threads to the info list.

    return info #This line returns the info list with the CPU Model and Cores or Threads count.


# Function to check disk usage for root ('/') partition
def get_disk_info():
    info = [] # store all the disk info we collect
    output = os.popen('df -h').readlines()  # run df -h to get disk info in human readable format

    for line in output[1:]:  # skip header
        parts = line.split() # splits the line 
        if len(parts) >= 6: # making sure it splits into 6 parts
            filesystem = parts[0] # the disk or partition name
            size = parts[1] #Total size of the partition
            used = parts[2] # Amount of space used
            available = parts[3] # Amount of space available
            percent_used = parts[4] #Usage Percentage
            mount_point = parts[5] # Where the partition is mounted

            if mount_point == '/':
                info.append("Filesystem: " + filesystem)
                info.append("Size: " + size)
                info.append("Used: " + used)
                info.append("Available: " + available)
                info.append("Usage: " + percent_used)
                info.append("Mounted on: " + mount_point)
                break #Found the root partition so no need to keep looping

    return info #send back the the collected info to the screen


def get_memory_info():  #this command defines a function named 'get_memory_info'
    info = []  #it creates an empty list to store memory details as strings for us to use later
    lines = os.popen('free -m').readlines() #this runs the 'free -m' command to check memory.'os.popen' is used to run command inside the terminal
    if len(lines) > 1: #making sure we have enough lines of output before trying to access them

        mem_line = lines[1].split()  #this command 'mem_line'contains the memory values in the 2nd line. It splits the line into words and numbers

        #extracting specific memory values from the list
        total = mem_line[1]  #total memory installed (in MB)
        used = mem_line[2]   #memory currently being used
        free = mem_line[3]   #memory currently free

        info.append("Total Memory: " + total + " MB") #getting the output as the total memory
        info.append("Used Memory: " + used + " MB") #output the total memory used
        info.append("Free Memory: " + free + " MB") #getting the total memory that is free
    return info  #returns the list of memory info, which gives us the final output


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
   
    users_info = get_logged_in_users() #calling the function to get user info
    for user in users_info: #looping through the list and printing the current username
        print(user)
    
   
    cpu_info = get_cpu_info() #This calls the function to get the CPU information.
    for line in cpu_info: #This line loops through all the lines in the info list.
        print(line) #This line prints the CPU Information line by line.


    memory_info = get_memory_info() # calling the get_memory_info() function
    for line in memory_info: #a loop to list all of the itms in memory_info
        print(line) # it will print all of the items in memory_info


    result = get_disk_info()
    for line in result:
        print(line)
    system_info = get_system_info()

    
    print("\nSystem Information:")
    print("------------------")
    for item in system_info:
        print(item)
    print()
