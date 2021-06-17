

def lengths_gen(y, x):
    '''A function that takes 2 x,y arguments
    and returns a list of x y-times'''
    Lengths = []
    count = 0
    for i in range(0,y):
        while count <y:
            Lengths.append(x)
            count+=1
    return Lengths



def list_appent(sub_list, y, base, List, x):
    '''The generator function is a matrix of nested lists.
    Receives as arguments a list of a sequence,
    an empty list to which adds nested lists,
    an argument to start iterating over the list
    '''
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
    '''Sequence generator function.
    Takes x, y as arguments and returns the generated list'''
    List=[number for number in range(1,x*y+1)]
    base = 0
    sub_list=[]
    list_appent(sub_list, y, base, List, x)
    print(sub_list)
    return sub_list



def get_data(intputdata):
    '''A function that takes a tuple object
    and iterates over this object passing each tapl
    to the function called in it.'''
    iterator=iter(intputdata)

    while True:
        try:
            for number_1, number_2 in iterator:
                list_gen(number_1, number_2)
            iterator.__next__()
        except StopIteration:
            break


def input_function(max_count=4):
    '''An input function that accepts 2 numbers per input.
    Returns a list of tupls each containing two numbers.
    It takes a number as an argument that determines the number of input requests.
    Validates the entered data.'''
    list_of_tuples = []
    start_count = 0
    current_count=max_count-start_count

    while start_count <max_count:
        input_data=input(
            f'''Please enter 4 entries of two numbers, for example "2.2". 
            You have {current_count} more inputs left: ''')

        list = [int(s) for s in input_data if s.isdigit()]
        if len(list)<2 :
            print(f'You are trying to enter:{input_data}')
            print('''It is necessary to enter data 
            \ras indicated in the example, please try again''')
        else:
            # list = [int(s) for s in input_data if s.isdigit()]
            # print(list)
            list_of_tuples.append(tuple(list[0:2]))
            start_count+=1
            current_count=max_count-start_count
    get_data(list_of_tuples)




input_function()
# You can pass an integer to this function,
# which will correspond to the number of input requests.