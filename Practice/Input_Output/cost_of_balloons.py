

def calc_minimum_cost_of_balloons(ballon_cost, participants_data):
    cost_of_using_green_ballon = 0
    cost_of_using_purple_ballon = 0
    for data in participants_data:
        if data[0] == '1':
            cost_of_using_green_ballon += ballon_cost[0]
            cost_of_using_purple_ballon += ballon_cost[1]
        if data[1] == '1':
            cost_of_using_green_ballon += ballon_cost[1]
            cost_of_using_purple_ballon += ballon_cost[0]

    return min(cost_of_using_green_ballon, cost_of_using_purple_ballon)


##############
testcases = int(input())
for _ in range(testcases):
    ballon_cost = list(map(int, input().split()))
    no_of_participants = int(input())
    participants_data = []
    for _ in range(no_of_participants):
        participants_data.append(list(input().split()))
    print(calc_minimum_cost_of_balloons(ballon_cost, participants_data))
##############
