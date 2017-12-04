#!/bin/python3

input_file = "day4_input"
data = ""

with open(input_file, 'r') as input_file:
    #data = input_file.readlines()
    data = input_file.read().splitlines()

def is_valid(passphrase):
    pass_list = passphrase.split()
    pass_seen = []
    for p in pass_list:
        if p not in pass_seen:
            pass_seen.append(p)
        else:
            return False
    return True

def is_valid_anagram(passphrase):
    pass_list = passphrase.split()
    pass_seen = []
    for p in pass_list:
        if sorted(p) not in pass_seen:
            pass_seen.append(sorted(p))
        else:
            return False
    return True

def count_valid_passphrases(passphrase_list):
    valid = 0
    for p in passphrase_list:
        if is_valid(p):
            valid += 1
    return valid

def count_valid_passphrases_anagram(passphrase_list):
    valid = 0
    for p in passphrase_list:
        if is_valid_anagram(p):
            valid += 1
    return valid

def unit_test_p1():
    print("Unit test start:")
    assert count_valid_passphrases(["aa bb cc dd ee"]) == 1
    print("Test 1 OK")
    assert count_valid_passphrases(["aa bb cc dd aa"]) == 0
    print("Test 2 OK")
    assert count_valid_passphrases(["aa bb cc dd aaa"]) == 1
    print("Test 3 OK")

def unit_test_p2():
    print("Unit test start:")
    assert count_valid_passphrases_anagram(["abcde fghij"]) == 1
    print("Test 1 OK")
    assert count_valid_passphrases_anagram(["abcde xyz ecdab"]) == 0
    print("Test 2 OK")
    assert count_valid_passphrases_anagram(["a ab abc abd abf abj"]) == 1
    print("Test 3 OK")
    assert count_valid_passphrases_anagram(["iiii oiii ooii oooi oooo"]) == 1
    print("Test 4 OK")
    assert count_valid_passphrases_anagram(["oiii ioii iioi iiio"]) == 0
    print("Test 5 OK")

print("My data:", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", count_valid_passphrases(data), "\n")

print("** Part two")
unit_test_p2()
print("My solution is: ", count_valid_passphrases_anagram(data), "\n")
