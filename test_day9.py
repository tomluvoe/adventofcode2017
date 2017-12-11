#!/bin/python3

from day9 import *

def test_p1():
    assert 1 == stream_processing('{}')
    assert 6 == stream_processing('{{{}}}')
    assert 5 == stream_processing('{{},{}}')
    assert 16 == stream_processing('{{{},{},{{}}}}')
    assert 1 == stream_processing('{<a>,<a>,<a>,<a>}')
    assert 9 == stream_processing('{{<ab>},{<ab>},{<ab>},{<ab>}}')
    assert 9 == stream_processing('{{<!!>},{<!!>},{<!!>},{<!!>}}')
    assert 3 == stream_processing('{{<a!>},{<a!>},{<a!>},{<ab>}}')

#{}, score of 1.
#{{{}}}, score of 1 + 2 + 3 = 6.
#{{},{}}, score of 1 + 2 + 2 = 5.
#{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
#{<a>,<a>,<a>,<a>}, score of 1.
#{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
#{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
#{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3

def test_p2():
    assert 0 == count_garbage('<>')
    assert 17 == count_garbage('<random characters>')
    assert 3 == count_garbage('<<<<>')
    assert 2 == count_garbage('<{!>}>')
    assert 0 == count_garbage('<!!>')
    assert 0 == count_garbage('<!!!>>')
    assert 10 == count_garbage('<{o"i!a,<{i<a>')

#<>, 0 characters.
#<random characters>, 17 characters.
#<<<<>, 3 characters.
#<{!>}>, 2 characters.
#<!!>, 0 characters.
#<!!!>>, 0 characters.
#<{o"i!a,<{i<a>, 10 characters
