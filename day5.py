#!/bin/python3

input_file = "day5_input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.readlines()
    data = [int(d) for d in data]

def count_jumps(jumps):
    ctr = 0
    count = 0
    while ctr >= 0 and ctr < len(jumps):
        count += 1
        jumps[ctr] += 1
        ctr += jumps[ctr] - 1
    return count

def count_jumps_2(jumps, feedback=False):
    ctr = 0
    count = 0
    while ctr >= 0 and ctr < len(jumps):
        count += 1
        if jumps[ctr] >= 3:
            jumps[ctr] -= 1
            ctr += jumps[ctr] + 1
        else:
            jumps[ctr] += 1
            ctr += jumps[ctr] - 1
    if feedback:
        return count, jumps
    return count

def unit_test_p1():
    test_data = [0, 3, 0, 1, -3]
    print("Unit test start:")
    assert count_jumps(test_data) == 5
    print("Test 1 OK")

def unit_test_p2():
    test_data = [0, 3, 0, 1, -3]
    print("Unit test start:")
    rv, test = count_jumps_2(test_data, True)
    assert rv == 10
    assert test == [2, 3, 2, 3, -1]
    print("Test 1 OK")

print("My data:", data, "\n")

part1 = data[:]
print("** Part one")
unit_test_p1()
print("My solution is:", count_jumps(part1), "\n")

part2 = data[:]
print("** Part two")
unit_test_p2()
print("My solution is:", count_jumps_2(part2), "\n")
