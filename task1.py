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

# inputdata =[(2,2), (3,3), (2,4)]
# get_data(inputdata)

def input_function(max_count=4):
    list_of_tuples = []
    start_count = 0
    current_count=max_count-start_count
    while start_count <max_count:
        input_data=input(f'Please enter 4 entries of two numbers, for example "2.2". You have {current_count} more inputs left: ')
        list = [int(s) for s in input_data if s.isdigit()]
        if len(list)<2 :
            print(f'You are trying to enter:{input_data}')
            print("It is necessary to enter data as indicated in the example, please try again")
        else:
            # list = [int(s) for s in input_data if s.isdigit()]
            # print(list)
            list_of_tuples.append(tuple(list[0:2]))
            start_count+=1
            current_count=max_count-start_count
    get_data(list_of_tuples)
    # print(list_of_tuples)

input_function()