import copy


def calc_minimum_operations(array, result_arr_size, array_size):
    operations = 0
    operations_arr = []
    dup_array = copy.deepcopy(array)
    for my_arr_number in array:
        if result_arr_size == 0:
            return len(dup_array)
        if has_three_factor(number=my_arr_number):
            result_arr_size -= 1
            dup_array.remove(my_arr_number)

    for dup_arr_number in dup_array:
        if dup_arr_number > 3:
            operations_arr.append(
                find_operations(number=dup_arr_number)
            )
        else:
            operations_arr.append(
                4 - dup_arr_number
            )
    # Sort the operatios array
    # operations_arr.sort()
    for i in xrange(0, result_arr_size):
        # operations += operations_arr[i]
        min_value = min(operations_arr)
        operations += min_value
        operations_arr.remove(min_value)
    operations += len(operations_arr)
    return operations


def find_operations(number):
    low = number - 1
    high = number + 1
    while True:
        if has_three_factor(number=low):
            return number - low
        elif has_three_factor(number=high):
            return high - number
        else:
            low -= 1
            high += 1


def has_three_factor(number):
    if number == 1:
        return False
    if check_perfect_square(number=number):
        if check_prime(number=int(number ** 0.5)):
            return True
    return False


# def check_prime(number):
#     if number > 1:
#         for i in xrange(2, number):
#             if (number % i) == 0:
#                 return False
#         else:
#             return True
#     else:
#         return True


def check_prime(number):
    if number in prime_numbers:
        return True
    return False


def check_perfect_square(number):
    sqrt = number ** 0.5
    if (int(sqrt) == sqrt):
        return True
    else:
        return False


def find_prime_number():
    prime_numbers = []
    for num in range(1, 998):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers


prime_numbers = find_prime_number()


my_input = map(int, raw_input().rstrip().split(' '))
array = map(int, raw_input().rstrip().split(' '))

print calc_minimum_operations(
    array=array, result_arr_size=my_input[1],
    array_size=my_input[0]
)
