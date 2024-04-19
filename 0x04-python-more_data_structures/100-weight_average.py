#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_sum = sum([x * y for x, y in my_list])
    weight_sum = sum([x for _, x in my_list])
    return total_sum / weight_sum
