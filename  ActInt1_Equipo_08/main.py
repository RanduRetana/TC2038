def suffix_array(string):
    sortedSuffixes = sorted([string[i:] for i in range(len(string))])
    return sortedSuffixes


def __main__():
    transmission1 = open("transmission1.txt", "r")
    transmission2 = open("transmission2.txt", "r")
    mcode1 = open("mcode1.txt", "r")
    mcode2 = open("mcode2.txt", "r")
    mcode3 = open("mcode3.txt", "r")

    subtransmission1 = suffix_array(transmission1.read())
    subtransmission2 = suffix_array(transmission2.read())

    for mcode1 in subtransmission1:
        if mcode1 in subtransmission1:
            print(mcode1)
            print("/n")
            print(subtransmission1)
            print("true")


__main__()


