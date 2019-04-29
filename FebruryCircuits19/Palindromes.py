
CONST = {}
CONST['total_palindrome'] = 0
CONST['previous_palindrome'] = 0


def check_palindrome(string):
    return string == string[::-1]


def do_operation(operation):
    for index, value in enumerate(operation):
        if index < 3:
            operation[index] = int(value)

    str1_index = (operation[1] ^ CONST['previous_palindrome']) - 1
    str2_index = (operation[2] ^ CONST['previous_palindrome']) - 1
    if operation[0] == 1:
        string_data[
            str1_index
        ] = string_data[str1_index] + string_data[str2_index]
        string_data[str2_index] = 0
        if memory_palindrome[str2_index]:
            CONST['total_palindrome'] -= 1
            memory_palindrome[str2_index] = 0
        if memory_palindrome[str1_index]:
            if not check_palindrome(string_data[str1_index]):
                CONST['total_palindrome'] -= 1
                memory_palindrome[str1_index] = 0
        else:
            if check_palindrome(string_data[str1_index]):
                CONST['total_palindrome'] += 1
                memory_palindrome[str1_index] = 1
    else:
        string_data[str1_index] = insert_char_to_string(
            string=string_data[str1_index], index=str2_index,
            char=operation[3]
        )
        if memory_palindrome[str1_index]:
            if not check_palindrome(string_data[str1_index]):
                CONST['total_palindrome'] -= 1
                memory_palindrome[str1_index] = 0
        else:
            if check_palindrome(string_data[str1_index]):
                CONST['total_palindrome'] += 1
                memory_palindrome[str1_index] = 1

    CONST['previous_palindrome'] = CONST['total_palindrome']
    return CONST['previous_palindrome']


def insert_char_to_string(string, index, char):
    return string[:index] + char + string[index:]


details = list(map(int, input().rstrip().split()))

string_data = []
memory_palindrome = []
operations = []
for index in range(details[0]):
    string = input()
    if check_palindrome(string=string):
        memory_palindrome.append(1)
        CONST['total_palindrome'] += 1
    else:
        memory_palindrome.append(0)
    string_data.append(string)

for _ in range(details[1]):
    temp = input().rstrip().split()
    for index, value in enumerate(temp):
        if index < 3:
            temp[index] = int(value)
    operations.append(temp)


for op in operations:
    print(do_operation(operation=op))
