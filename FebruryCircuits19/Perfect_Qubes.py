

def calc_product_of_array(array):
    result = 1
    for element in array:
        result *= element
    return result


def check_perfect_cube(number):
    qube_root = number ** (1 / 3)
    return True if round(qube_root) ** 3 == number else False


def get_perfect_cube(array):
    result = 0
    length = len(array)


N = int(input())

numbers_array = []
for _ in range(N):
    temp = list(set(list(map(int, input().rstrip().split()))))
    numbers_array.append(calc_product_of_array(array=temp))
