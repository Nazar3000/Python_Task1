import logging

def lengths_gen(y, x):
    Lengths = []
    count = 0
    for i in range(0,y):
        while count <y:
            Lengths.append(x)
            count+=1
    print(Lengths)
    # logging.warning(f"{Lengths}")
    return Lengths

lengths_gen(4,2)