import random


def ran_16_card_num():
    card_nums = []
    total = 0
    for i in range(15):
        num = random.randint(0,9)
        card_nums.append(str(num))
        total += (num * (i+1))
    check_digit = total % 10
    card_nums.append(str(check_digit))
    card_num = int("".join(card_nums))
    return card_num

class Base_Account():
    def __init__(self):
        self.account_number = ran_16_card_num()
        self.account_cards = []
        self.account_balance = 0
    def load(num,cards,bal,loans):
        self.account_number = num
        self.account_cards = cards
        self.account_balance = bal
def Simple_Account(Base_Account):
    def __init__(self):
        super().__init__()
        self.loans = []
        def load(num,cards,bal,loans):
        self.account_number = num
        self.account_cards = cards
        self.account_balance = bal
        self.loans = loans
