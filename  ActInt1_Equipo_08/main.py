def suffix_array(string):
    sortedSuffixes = sorted([string[i:] for i in range(len(string))])
    return sortedSuffixes

def mcodeSearch(mcode, transmission):
    start = 0
    while True:
        start = transmission.find(mcode, start)
        if start == -1: return
        end = start + len(mcode) - 1
        print("True ", start, end)
        start += 1

def __main__():
    transmissions = []
    mcodes = []
    for i in range(1, 3):
        with open(f"transmission{i}.txt", "r") as f:
            transmissions.append(f.read())
    for i in range(1, 4):
        with open(f"mcode{i}.txt", "r") as f:
            mcodes.append(f.read())

    for i, mcode in enumerate(mcodes):
        for j, transmission in enumerate(transmissions):
            print(f"mcode{i+1} in transmission{j+1}")
            if mcode in transmission:
                mcodeSearch(mcode, transmission)
            else:
                print("False")

__main__()



