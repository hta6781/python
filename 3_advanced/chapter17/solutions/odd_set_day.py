"""
Given a set, remove all the even numbers from
it, and for each even number removed, add
"Removed [insert the even number you removed]".
Example: {1,54, 2, 5} becomes {"Removed 54", 1,
5, "Removed 2"}. It is possible to solve this
problem using either discard or remove.
"""


def odd_set_day(given_set):
    add_remove = []
    for elem in given_set:
        if elem % 2 == 0:
            add_remove.append(elem)
    for remove in add_remove:
        given_set.remove(remove)
        given_set.add("Removed " + str(remove))


given_set = {1, 2, 4, 5}
odd_set_day(given_set)
print(given_set)
