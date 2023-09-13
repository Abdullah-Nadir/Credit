
# Credit

A program in python that prompts the user to enter a credit card number, validates its authenticity, and identifies the card type.


## Luhn’s Algorithm

According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:

- Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
- Add the sum to the sum of the digits that weren’t multiplied by 2.
- If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!

## Implementation Details

In a file called `credit.c`, there's a program that prompts the user for a credit card number and then reports (via printf) whether it is a valid American Express, MasterCard, or Visa card number.
## Usage/Examples



```
$ ./credit
Number: 4003600000000014
VISA
```

```
$ python credit.py
Number: 378282246310005
AMEX
```

```
$ ./credit
Number: 4003-6000-0000-0014
Number: foo
Number: 4003600000000014
VISA                                                          
```

```
$ ./credit
Number: 6176292929
INVALID
```
