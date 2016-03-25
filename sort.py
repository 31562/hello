# generate random numbers
def gen_ran(num):
    import random
    input_ran = [0] * num
##    for n in range(0, len(input)):
##        input[n] = random.randint(1, 100)
    input_ran = random.sample(xrange(100),num)

    return input_ran

input = gen_ran(10)

#sort
def sort(input):
    output = input[:]
    for a in range(2, len(input)):

        for b in range(a, 0, -1):

            if output[b-1] > output[b]:
                output[b], output[b-1] = output[b-1], output[b]

    return output

print input
print sort(input)


