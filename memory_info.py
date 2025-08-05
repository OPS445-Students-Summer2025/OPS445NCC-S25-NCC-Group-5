#!/usr/bin/env python3

import os #this is os module to use os related commands


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


if __name__ == '__main__':
    memory_info = get_memory_info() # calling the get_memory_info() function
    for line in memory_info: #a loop to list all of the itms in memory_info
        print(line) # it will print all of the items in memory_info
