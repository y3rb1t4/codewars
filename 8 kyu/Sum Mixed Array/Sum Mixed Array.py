def sum_mix(arr):
    result = 0
    for i in arr:
        try:
            result += i
        except TypeError:
            result += int(i)
    return result 