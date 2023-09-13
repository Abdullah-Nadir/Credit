from cs50 import get_int


def main():
    # Taking input from the user
    n = get_int("Number: ")

    # Finding the total_sum of the number
    sum = calc_sum(n)

    # Printing The results
    if sum % 10 == 0:
        result = check_card_type(n)
        print(result)
    else:
        print("INVALID")


# Finding the total_sum of the credit card number
def calc_sum(n):
    total_sum = 0
    odd = False  # Flag do determine whether the current digit is on odd index or not

    while n > 0:
        digit = n % 10
        n //= 10

        # Selecting the number’s second-to-last digit
        if odd:
            digit *= 2
            if digit >= 10:
                digit = digit % 10 + 1

        total_sum += digit
        odd = not odd

    return total_sum


# Function for checking card type
def check_card_type(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10

    l = len(digits)

    if l == 15 and digits[-1] == 3 and digits[-2] in {4, 7}:
        return "AMEX"
    elif l == 16 and digits[-1] == 5 and 1 <= digits[-2] <= 5:
        return "MASTERCARD"
    elif (l == 13 or l == 16) and digits[-1] == 4:
        return "VISA"
    else:
        return "INVALID"


main()
