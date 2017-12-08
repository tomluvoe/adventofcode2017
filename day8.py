#!/bin/python3

import re

test_data = ["b inc 5 if a > 1", "a inc 1 if b < 5", "c dec -10 if a >= 1", "c inc -20 if c == 10"]

input_file = "day8_input"
data = ""

registers = {}
max_registers = {}

def eval_condition(condition):
    if condition[0] in registers:
        rv = eval('registers[\"'+condition[0]+'\"]'+condition[1]+'int('+condition[2]+')')
    else:
        rv = eval('int(0)'+condition[1]+'int('+condition[2]+')')
    return rv

def change_reg(register, step):
    #print('change reg:',register,step)
    if register in registers:
        registers[register] += int(step)
        if max_registers[register] < registers[register]:
            max_registers[register] = registers[register]
    else:
        #print('Set',register,'to',step)
        max_registers[register] = int(step)
        registers[register] = int(step)

def inc(register, step, condition):
    if eval_condition(condition):
        change_reg(register, step)
    #print('inc',register,step,condition)

def dec(register, step, condition):
    if eval_condition(condition):
        change_reg(register, int(-1*int(step)))
    #print('dec',register,step,condition)

def run(data):
    for cmd in data:
        #print("Run", list(cmd))
        eval(cmd[1]+'(cmd[0],cmd[2],cmd[3:6])')
    maxval = 0
    for k in registers.keys():
        if registers[k] > maxval:
            maxval = registers[k]
    return maxval

with open(input_file, 'r') as input_file:
    data = input_file.readlines()
    data = [d.strip() for d in data]
    #print(data)

def parse_data(data):
    #p = re.compile(r'([a-z]+) ([inc|dec]) (-?[0-9]+) (.*)')
    p = re.compile(r'([a-z]+) (inc|dec) ([-|0-9]*) if ([a-z]*) (\W*) ([-|0-9]*)')
    my_data = []
    for d in data:
        if p.match(d):
            my_data.append(p.match(d).groups())
    return my_data

def unit_test_p1(data):
    my_data = parse_data(data)
    print("Unit test start:")
    #print(my_data)
    assert run(my_data) == 1
    print("Test 1 OK")

def print_max(max_registers):
    maxval = 0
    for k in max_registers.keys():
        if max_registers[k] > maxval:
            maxval = max_registers[k]
    return maxval

print("** Part one")
unit_test_p1(test_data)
my_data = parse_data(data)
print("My solution is:", run(my_data))

print("\n** Part two")
print("My solution is:", print_max(max_registers))
