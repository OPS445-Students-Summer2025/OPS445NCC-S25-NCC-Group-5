#!/usr/bin/env python3

import os  #importing os module to run os related commands

def get_logged_in_users(): #this function checks who is currently logged into the system 
    users = [] #creating an empty list to hold our output lines

    output = os.popen('who').readlines() #running the who command to get logged in user  and read its lines

    for line in output: #loop through each line from the 'who' command output
        parts = line.split() #spliting the line into words to isolate the username 
        if len(parts) >= 1:
            username = parts[0]
            users.append("Currently logged in user: " + username)  #adding the username

    return users  #returns the list of user info lines

if __name__ == '__main__':
    users_info = get_logged_in_users() #calling the function to get user info
    for user in users_info: #looping through the list and printing the current username
        print(user)
