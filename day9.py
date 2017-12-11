#!/bin/python3

input_file = "day9_input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read().strip()

def stream_processing(data):
    state = 1
    score = 0
    garbage = False
    c = 0
    while c < len(data):
        if data[c] == '!':
            c += 1
        elif not garbage and data[c] == '<':
            garbage = True
        elif garbage and data[c] == '>':
            garbage = False
        elif not garbage and data[c] == '{':
            score += state
            state += 1
        elif not garbage and data[c] == '}':
            state -= 1
        c += 1
    return score

def count_garbage(data):
    score = 0
    garbage = False
    c = 0
    while c < len(data):
        if data[c] == '!':
            c += 1
        elif not garbage and data[c] == '<':
            garbage = True
        elif garbage and data[c] == '>':
            garbage = False
        elif garbage:
            score += 1
        c += 1
    return score

print("My data:", data)

print("\n** Part one")
print("My solution is:", stream_processing(data))

print("\n** Part two")
print("My solution is:", count_garbage(data))
