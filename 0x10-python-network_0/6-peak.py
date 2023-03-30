#!/usr/bin/python3
"""
This function finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    This function finds a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None

    li = list_of_integers
    i = 1
    k = li[i]
    while i < len(li) - 1:
        if (li[i - 1] <= li[i] and li[i + 1] <= li[i] and li[i] > k):
            k = li[i]
        i += 1

    return k
