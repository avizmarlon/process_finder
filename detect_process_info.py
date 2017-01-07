import re
import os

# Dict Version
pids = {}
proc_list = os.popen('tasklist').readlines()

for proc in proc_list:
    # finds all pids of the current iteration
    pid = re.findall('.* ([0-9]+) [a-zA-Z]', proc)

    # finds all the process names of the current iteration
    pname = re.findall('^\S+', proc)

    # this section is in the case that a process has multiple instances and thus multiple pids with the same pname
    if pname in pids == True:
        if type(pids[pname]) == list:
            pids[pname].extend(pid)
        # pname value becomes a list in case its not a list yet
        current_pname_value = pids[pname]
        pids[pname] = [current_pname_value, pid]
    else:
        pids[pname] = pid