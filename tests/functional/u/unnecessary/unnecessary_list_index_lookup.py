"""Tests for unnecessary-list-index-lookup."""

# pylint: disable=missing-docstring, too-few-public-methods, expression-not-assigned, line-too-long, unused-variable

my_list = ['a', 'b']

for idx, val in enumerate(my_list):
    print(my_list[idx]) # [unnecessary-list-index-lookup]

for idx, _ in enumerate(my_list):
    print(my_list[0])
    if idx > 0:
        print(my_list[idx - 1])

for idx, val in enumerate(my_list):
    del my_list[idx]

for idx, val in enumerate(my_list):
    my_list[idx] = 42

for vals in enumerate(my_list):
    # This could be refactored, but too complex to infer
    print(my_list[vals[0]])

def process_list(data):
    for index, value in enumerate(data):
        index = 1
        print(data[index])

def process_list_again(data):
    for index, value in enumerate(data):
        value = 1
        print(data[index]) # Can't use value here, it's been redefined

other_list = [1, 2]
for idx, val in enumerate(my_list):
    print(other_list[idx])

OTHER_INDEX = 0
for idx, val in enumerate(my_list):
    print(my_list[OTHER_INDEX])

result = [val for idx, val in enumerate(my_list) if my_list[idx] == 'a'] # [unnecessary-list-index-lookup]
result = [val for idx, val in enumerate(my_list) if idx > 0 and my_list[idx - 1] == 'a']
result = [val for idx, val in enumerate(my_list) if other_list[idx] == 'a']
result = [my_list[idx] for idx, val in enumerate(my_list)] # [unnecessary-list-index-lookup]
