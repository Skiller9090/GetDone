import random
import Account

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


