from Account import *


def base_account_create():
    global accounts
    new_account = Base_Account()
    new_account_num = new_account.get_all_info()[0]
    to_add = {new_account_num:new_account}
    return to_add

