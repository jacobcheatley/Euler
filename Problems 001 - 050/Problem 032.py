# TODO: Make this something other than the most inefficient solution ever made for anything ever

from itertools import permutations
from custom.math import tuple_to_int

numbers = list("123456789")
final = []

for i in range(1, 10):
    for first in permutations(numbers, i):
        remaining_one = [x for x in numbers if x not in first]
        for j in range(1, 10 - i):
            for second in permutations(remaining_one, j):
                remaining_two = [x for x in remaining_one if x not in second]
                for possible_prod in permutations(remaining_two):
                    chicken = tuple_to_int(possible_prod)
                    if tuple_to_int(first) * tuple_to_int(second) == chicken:
                        final.append(chicken)

print(sum(set(final)))
