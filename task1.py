import logging

def lengths_gen(y, x):
    Lengths = []
    count = 0
    for i in range(0,y):
        while count <y:
            Lengths.append(x)
            count+=1
    # print(Lengths)
    # logging.warning(f"{Lengths}")
    return Lengths

# lengths_gen(4,2)


def list_appent(sub_list, y, base, List, x):
    Lengths = lengths_gen(y, x)
    iterator=iter(Lengths)
    while True:
        try:
            iterator.__next__()
            for num in Lengths:
                if List[base:num + base] >[]:
                    sub_list.append(List[base:num + base])
                    base += num
        except StopIteration:
            break
    return sub_list



def list_gen(y,x):
    List=[number for number in range(1,x*y+1)]
    base = 0
    sub_list=[]
    list_appent(sub_list, y, base, List, x)
    print(sub_list)
    return sub_list



def get_data(intputdata):
    iterator=iter(intputdata)
    while True:
        try:
            for number_1, number_2 in iterator:
                list_gen(number_1, number_2)
            iterator.__next__()
        except StopIteration:
            break

inputdata =[(2,2), (3,3), (2,4)]
get_data(inputdata)