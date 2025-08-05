#!/usr/bin/env python3
import os  # importing the os module so we can run commands like 'df -h'

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

if __name__ == "__main__":
    result = get_disk_info()
    for line in result:
        print(line)
