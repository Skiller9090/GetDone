from random_numbers import *

class Base_Account():
    def __init__(self):
        self.account_number = ran_16_card_num()
        self.account_cards = []
        self.account_balance = 0
    def load(num,cards,bal,loans):
        self.account_number = num
        self.account_cards = cards
        self.account_balance = bal
