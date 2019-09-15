

def get_all_info(account_obj):
    info = account_obj.get_all_info()
    acc_num = info[0]
    cards = info[1]
    bal = info[2]
    return acc_num,cards,bal
    print("Account Number:",end=" ")
    print(acc_num)
    print("Account Cards:",end=" ")
    print(cards)
    print("Account Balance: £",end="")
    print(bal)
