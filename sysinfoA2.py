#!/usr/bin/env python3
"""
Author: Sultan Mahamud
"""

import os
import sys

def get_system_info():
    info = []

    hostname = os.popen('hostname').read().strip()
    info.append("Hostname: " + hostname)

    os_info = os.popen('uname -o').read().strip()
    info.append("Operating System: " + os_info)

    kernel = os.popen('uname -r').read().strip()
    info.append("Kernel Version: " + kernel)

    uptime = os.popen('uptime -p').read().strip()
    info.append("Uptime: " + uptime)

    return info

def main():
    system_info = get_system_info()
    for item in system_info:
        print(item)

if __name__ == "__main__":
    main()