#!/bin/python3

input_file = "day2_input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.readlines()

def checksum_single_row(row):
    items = [int(i) for i in row.split()]
    return max(items) - min(items)

def divide_single_row(row):
    items = [int(i) for i in row.split()]
    for i in items:
        for j in items:
            if float(i)/j == int(float(i)/j) and i != j:
                return int(i/j)

def checksum(docs):
    chksum = 0
    for row in docs:
        chksum += checksum_single_row(row)
    return chksum

def checksum_divide(docs):
    chksum = 0
    for row in docs:
        chksum += divide_single_row(row)
    return chksum

def unittest_1():
    doc = ["5 1 9 5", "7 5 3", "2 4 6 8"]
    print("Unit test start:")
    assert checksum_single_row(doc[0]) == 8
    print("Test 1 OK")
    assert checksum_single_row(doc[1]) == 4
    print("Test 2 OK")
    assert checksum_single_row(doc[2]) == 6
    print("Test 3 OK")
    assert checksum(doc) == 18
    print("Test 4 OK")

def unittest_2():
    doc = ["5 9 2 8", "9 4 7 3", "3 8 6 5"]
    print("Unit test start:")
    assert divide_single_row(doc[0]) == 4
    print("Test 1 OK")
    assert divide_single_row(doc[1]) == 3
    print("Test 2 OK")
    assert divide_single_row(doc[2]) == 2
    print("Test 3 OK")
    assert checksum_divide(doc) == 9
    print("Test 4 OK")

print("My data:", data, "\n")

print("** Part one")
unittest_1()
print("My solution is: ", checksum(data), "\n")

print("** Part two")
unittest_2()
print("My solution is: ", checksum_divide(data))
