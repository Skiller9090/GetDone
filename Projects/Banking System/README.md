Banking Management System

TODO: Design its architecture


# Built-in variables ,function , classes:

ran_16_card_num() = Function which makes a random credit card number (16 digits) with the 16th digit being a check digit which uses a wieghted sum MOD 10 to create it.

Base_Account = Base Class for all future types of accounts which has card_numbers,account_number and account_balance built in.

Simple_Account = Inherits from Base_Account but adds loans.
