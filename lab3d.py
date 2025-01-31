#!/usr/bin/env python3

#Author ID: rnagarasa

import os

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    output  = os.popen(command).read().strip()
    return output
