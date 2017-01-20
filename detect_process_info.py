import re
import os
import pyperclip
import time

# Dict Version
pids = {}
proc_list = os.popen('tasklist').readlines()

for proc in proc_list:
    # finds all the process names of the current iteration
    pname = re.findall('^(.*?) [0-9]+', proc)
    if len(pname) == 0:
        continue
    pname = pname[0].strip()
    
    # finds all pids of the current iteration
    pid = re.findall('.* ([0-9]+) [a-zA-Z]+', proc)
    
    # this section is in the case that a process has multiple instances and thus multiple pids with the same pname    
    if pname in pids:
        if type(pids[pname]) == list:
            pids[pname].extend(pid)
            
        # pname value becomes a list in case its not a list yet
        else:
            current_pname_value = pids[pname]
            pids[pname] = [current_pname_value, pid]
    else:
        pids[pname] = pid
 
 
# for tests
for process in pids:
    print("Process:", process, "\nPID(s):")
    for pid in pids[process]:
        print(pid)
    print('\n')
