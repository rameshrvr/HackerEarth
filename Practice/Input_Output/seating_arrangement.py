
def find_seat_details(seat_number):
    compartment_number = seat_number // 12
    seat_number = seat_number % 12
    seat_position = ''
    if seat_number % 6 in [0, 1]:
        seat_position = 'WS'
    elif seat_number % 6 in [2, 5]:
        seat_position = 'MS'
    else:
        seat_position = 'AS'

    if seat_number == 0:
        opposite_seat = ((compartment_number - 1) * 12) + 1
    else:
        opposite_seat = (compartment_number * 12) + (12 - seat_number + 1)
    return ' '.join([str(opposite_seat), seat_position])


#########
test_cases = int(input())

for _ in range(test_cases):
    seat_number = int(input())
    print(find_seat_details(seat_number))
#########
