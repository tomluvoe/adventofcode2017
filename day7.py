#!/bin/python3

import re

input_file = "day7_input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.readlines()

def parse_indata(data):
    p1 = re.compile(r'\s*(.*) \((.*?)\)')
    p2 = re.compile(r'\s*(.*) \((.*?)\) -> (.*)')
    parsed_data = []
    for d in data:
        d.strip()
        #print(d)
        #name, weight, above = p.match(d)
        if p2.match(d):
            name = p2.match(d).group(1)
            weight = p2.match(d).group(2)
            above = p2.match(d).group(3)
            parsed_data.append([name, weight, above.replace(',','').split()])
        elif p1.match(d):
            name = p1.match(d).group(1)
            weight = p1.match(d).group(2)
            parsed_data.append([name, weight, []])
    return parsed_data

def find_root(data):
    aboves = []
    for d in data:
        if d[2] is not []:
            aboves.extend(d[2])
    for d in data:
        if d[0] not in aboves:
            return d[0]
    return False

def find_incorrect_weight(data):
    pass

def get_testdata():
    test_data = \
"""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""
    return test_data.split("\n")

def unit_test_p1(data):
    print("Unit test start:")
    assert find_root(data) == 'tknk'
    print("Test 1 OK")

#print(get_testdata())
#print(parse_indata(get_testdata()))

print("** Part one")
unit_test_p1(parse_indata(get_testdata()))
print("My solution is:", find_root(parse_indata(data)))
