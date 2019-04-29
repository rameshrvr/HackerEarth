

prob_details = list(map(int, input().rstrip().split()))
n, m = prob_details[0], prob_details[1]
details = {}

for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    if details.get(temp[1]):
        if details[temp[1]] < temp[0]:
            details[temp[1]] = temp[0]
    else:
        details[temp[1]] = temp[0]

print(sum(details.values()))
