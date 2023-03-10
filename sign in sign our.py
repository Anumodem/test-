
def processLogs(logs, maxSpan):
    # Write your code here
    signin = {}
    signout = {}
    for i in logs:
        uid, time, action = i.split()
        if action == "sign-out":
            signout [uid] = int(time)
        else:
            signin [uid] = int(time)
    lens = []
    for i, j in signout.items():
        if i in signin:
            time = j - signin[i]
            if time<=maxSpan:
                lens.append(int(i))
    lens.sort()
    res = [str(i) for i in lens]
    return res
