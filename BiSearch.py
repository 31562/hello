def gen_ran(num):
    import random
    input_ran = random.sample(xrange(10000), num)
    return input_ran

def BinarySearch(array1, num1, n_start, n_end):
    if n_start != n_end:
        current = int((n_start+n_end)/2)

        if array1[current] > num1:
            n_start_new, n_end_new = n_start, int((n_end - n_start)/2) + n_start
        elif array1[current] < num1:
            n_start_new, n_end_new = int((n_end - n_start)/2) + 1 + n_start, n_end
        else:
            n_start_new, n_end_new = current, current

        BinarySearch(array1, num1, n_start_new, n_end_new)

        return n_start_new, n_end_new
    else:
        print n_start

length = 15 
#array size
SearchArray = gen_ran(length)

import random
SearchNum = SearchArray[random.randint(0, length-1)]

SortedArray = sorted(SearchArray)
BinarySearch(SortedArray, SearchNum, 0, len(SortedArray)-1)
