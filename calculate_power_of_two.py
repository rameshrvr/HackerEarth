
MODULO = 1000000007


def calc_power_of_two(number):
    # i have taken 60 as base number for 64 bit processor
    if number <= 60:
        # Fastest way to calculate 2^N is to left shift binary 1 to N times
        return (1 << number) % MODULO
    quotient = int(number / 60) % MODULO
    reminder = number % 60
    two_power_sixty = 1 << 60
    # We can represent 2^N as 2^((quotient * 60) + reminder)
    # RESULT = quotient * (2^60) * (2^reminder)
    return ((quotient * two_power_sixty) % MODULO * (1 << reminder)) % MODULO


if __name__ == '__main__':
    number = int(input("Enter any number: "))
    print(calc_power_of_two(number=number))
