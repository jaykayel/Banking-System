import os
import terminal
import login
from pathlib import Path
import random


class Create:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin

    def check(self, card_number):
        card = Path(f"private-keys/{card_number}.pvk")
        single = False
        if card.is_file():
            single = True
        while single == True:
            inn = 400000
            ai = random.randint(100000000, 999999999)
            cs = random.randint(0, 9)
            card_number = f'{inn}{ai}{cs}'

    def complete(self):
        print('Your card has successfully been created!')
        print('Your card number is:')
        print(card_number)
        print('Your pin is:')
        print(pin)

class Safe:

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin

    def session(self):
        with open('temp', 'w') as f:
            f.write(card_number)
            f.write('\n')
            f.write(pin)

    def safe(self):
        with open("cards/" + f'{card_number}.cred', 'a') as f:
            f.write(card_number)
            f.write('\n')
            f.write(pin)
            f.write('\n')
            f.write('1000')
            f.write('\n')
            f.close()


# generating card_number
inn = 400000
ai = random.randint(100000000, 999999999)
cs = random.randint(0, 9)
card_number = f'{inn}{ai}{cs}'

# generating pin
pin0 = random.randint(0, 9)
pin1 = random.randint(0, 9)
pin2 = random.randint(0, 9)
pin3 = random.randint(0, 9)
pin = f'{pin0}{pin1}{pin2}{pin3}'

# check for doubles
card = Create(card_number, pin)
card.check(card_number)

# safe card file
card = Safe(card_number, pin)
card.safe()

# generate session file
card = Safe(card_number, pin)
card.session()

# generate card
card = Create(card_number, pin)
card.complete()