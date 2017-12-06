#!/bin/python3

import operator

input_file = "day6_input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read().split()
    data = [int(d) for d in data]

def redistribute(memory, cycles = False):
    my_mem = memory[:]
    seen_list = []
    loops = 0
    while my_mem not in seen_list:
        loops += 1
        seen_list.append(my_mem[:])
        index, value = max(enumerate(my_mem), key=operator.itemgetter(1))
        my_mem[index] = 0
        while value > 0:
            index += 1
            my_mem[index%len(my_mem)] += 1
            value -= 1
    if cycles:
        return len(seen_list)-seen_list.index(my_mem)
    return loops

def unit_test_p1():
    test = [0, 2, 7, 0]
    print("Unit test start:")
    assert redistribute(test) == 5
    print("Test 1 OK")

def unit_test_p2():
    test = [0, 2, 7, 0]
    print("Unit test start:")
    assert redistribute(test, cycles=True) == 4
    print("Test 1 OK")

print("** Part one")
unit_test_p1()
print("My solution is:", redistribute(data), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", redistribute(data, True), "\n")
