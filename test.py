#!/usr/bin/env python3

import sys
import re
import operator

error_messages = {}
user_entries = {}

with open("syslog.log") as f:
    for line in f:
        if "ERROR " in line:
            match = re.search(r'ERROR [\w \[]*)', line)
            if match is not None:
                res = match.group(0).replace("ERROR ", "").strip()
                if res == "Ticket":
                    res = "Ticket doesn't exist"
                if not res in error_messages:
                    error_messages[res] = 1
                else:
                    error_messages[res] += 1

        elif " INFO " in line:
            match = re.search(r'\(.*?\)', line)
            user_s = match.group(0)
            user = user_s.strip("()")
            if not user in user_entries:
                user_entries[user] = 1
            else:
                user_entries[user] += 1
