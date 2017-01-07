# List Version
pids = []
proc_list = os.popen('tasklist').readlines()

for proc in proc_list:
    # finds all pids of the current iteration
    pid = re.findall('.* ([0-9]+) [a-zA-Z]', proc)

    # finds all the process names of the current iteration
    pname = re.findall('^\S+', proc)

    # adds a (pname, pid) tuple pair to the list
    pids.append((pname[0], pid[0]))