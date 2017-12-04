#!/bin/python3

data = 347991

def get_layer_with_square(square):
    if square <= 0:
        return -1, -1, -1, -1
    last_layer_high = 1
    last_layer_size = 1
    layer_id = 0
    if square == 1:
        return 0, 1, 1, 0
    while True:
        current_layer_size = ((last_layer_size-1)/4 + 1) * 4 + 4
        #print(layer_id,": ",current_layer_size," ",last_layer_high+1,"->",last_layer_high+current_layer_size)
        if last_layer_high+1 <= square < last_layer_high+1+current_layer_size:
            return last_layer_high+1, current_layer_size, last_layer_high+current_layer_size, layer_id
        last_layer_high += current_layer_size
        last_layer_size = current_layer_size+1
        layer_id += 1

def distance_to_origo(square):
    if square == 1:
        return 0
    layer = get_layer_with_square(square)
    #print(square, layer)
    while square >= layer[1]/4+layer[0]:
        square -= layer[1]/4
    #print(abs(square-layer[0]-layer[3]),abs(layer[1]/4/2))
    return int(abs(square-layer[0]-layer[3]) + abs(layer[1]/4/2))

def unit_test_p1():
    print("Unit test start:")
    assert distance_to_origo(1) == 0
    print("Test 1 OK")
    assert distance_to_origo(12) == 3
    print("Test 2 OK")
    assert distance_to_origo(23) == 2
    print("Test 3 OK")
    assert distance_to_origo(2) == 1
    assert distance_to_origo(3) == 2
    assert distance_to_origo(4) == 1
    assert distance_to_origo(5) == 2
    assert distance_to_origo(6) == 1
    assert distance_to_origo(7) == 2
    assert distance_to_origo(8) == 1
    assert distance_to_origo(9) == 2
    assert distance_to_origo(10) == 3
    assert distance_to_origo(11) == 2
    print("Test 3.5 OK")
    assert distance_to_origo(1024) == 31
    print("Test 4 OK")

#find_xy_coordinate(15)
print("My data:", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", distance_to_origo(data), "\n")
