list = input('Enter a list of numbers separated by a space').split(' ')
num_list = [int(i) for i in list]


def max(list):

    max = float('-inf')
    for num in list:
        if num > max:
            max = num

    return max


def min(list):

    min = float('inf')
    for num in list:
        if num < min:
            min = num

    return min


print(f" Maximum: {max(num_list)} \n Minimum: {min(num_list)}")
