#!/bin/python3

input_file = "day1_input"

with open(input_file, 'r') as input_file:
    data = input_file.read()
    data = data[:-1]

def captcha(data, delta=1):
    captcha_sum = 0
    for i in range(len(data)):
        if data[i] == data[(i+delta)%len(data)]:
            captcha_sum += int(data[i])
    return captcha_sum

def unit_test_p1():
    print("Unit test start:")
    assert 3 == captcha("1122")
    print("Test 1 OK")
    assert 4 == captcha("1111")
    print("Test 2 OK")
    assert 0 == captcha("1234")
    print("Test 3 OK")
    assert 9 == captcha("91212129")
    print("Test 4 OK")

def unit_test_p2():
    print("Unit test start:")
    assert 6 == captcha("1212", 2)
    print("Test 1 OK")
    assert 0 == captcha("1221", 2)
    print("Test 2 OK")
    assert 4 == captcha("123425", 3)
    print("Test 3 OK")
    assert 12 == captcha("123123", 3)
    print("Test 4 OK")
    assert 4 == captcha("12131415", 4)
    print("Test 5 OK")

print("My data:", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", captcha(data), "\n")

print("** Part two")
unit_test_p2()
print("My solution is: ", captcha(data, int(len(data)/2)))
