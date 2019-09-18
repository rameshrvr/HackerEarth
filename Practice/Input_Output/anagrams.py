import string


def find_no_of_deletions(string1, string2):
    str1_dict = {}
    str2_dict = {}
    for char in list(string1):
        if char in str1_dict:
            str1_dict[char] += 1
        else:
            str1_dict[char] = 1

    for char in list(string2):
        if char in str2_dict:
            str2_dict[char] += 1
        else:
            str2_dict[char] = 1

    result = 0
    for char in list(string.ascii_lowercase):
        if char in str1_dict and char not in str2_dict:
            result += str1_dict[char]
        elif char in str2_dict and char not in str1_dict:
            result += str2_dict[char]
        elif char in str1_dict and char in str2_dict:
            result += abs(str1_dict[char] - str2_dict[char])

    return result


##########
test_cases = int(input())

for _ in range(test_cases):
    string1 = input()
    string2 = input()
    print(find_no_of_deletions(string1=string1, string2=string2))
##########
