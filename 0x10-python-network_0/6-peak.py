#!/usr/bin/python3
def find_peak(list_of_integers):
    find_peak = __import__('6-peak.txt').find_peak
    '''
    args:
    list_of_integers(int): list of the integers where peak is to be found
    Return: list_of_integers peak, else nothing (None)
    '''
    size = len(list_of_integers)
    midx = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        midx = midx // 2
        if (mid < size - 1 and list_of_integers[mid] < list_of_integers[mid + 1]):
            if midx // 2 == 0:
                midx = 2
            mid = mid + midx // 2
        elif midx > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if midx // 2 == 0:
                midx = 2
            mid = mid + midx // 2
        else:
            return list_of_integers[mid]
