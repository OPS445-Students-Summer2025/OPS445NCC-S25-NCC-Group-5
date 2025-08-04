#!/usr/bin/env python3
"""
Author: Sultan Mahamud
"""

import os
import sys

def get_system_info():
    info = []
#Systen' hostname 
    hostname = os.popen('hostname').read().strip()
    info.append("Hostname: " + hostname)
#OS information
    os_info = os.popen('uname -o').read().strip()
    info.append("Operating System: " + os_info)
#Kernel Version information
    kernel = os.popen('uname -r').read().strip()
    info.append("Kernel Version: " + kernel)

    uptime = os.popen('uptime -p').read().strip()
    info.append("Uptime: " + uptime)

    return info

