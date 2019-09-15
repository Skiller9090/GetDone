Banking Management System

TODO: Design its architecture


## Architecture

Every one of us shall choose a functionality each of us will program. 

The program shall have a menu listing all of its user-available functionality --- i.e., Create Account, Close Account, Withdraw, Tranfer, Exit etc. The main program will simply call such functions, as such the implementation itself will entirely rely on every one us: one must create their own file where they implement such features, e.g., CreateAccount.py, Exit.py, Transfer.py.

Main.py must call such functions, e.g., 

```python
import CreateAccount
import CloseAccount
import Transfer
import Exit
import Withdraw

if command == "Create Account": 
  CreateAccount()
  
if command == "Close Account": 
  CloseAccount()
  
if command == "Transfer": 
  Transfer()

if command == "Exit": 
  Exit()
```


All such features shall work around a **core system**. If one wants to transfer or withdraw, for example, they will need to call **built-in variables** in order to accomplish so. For example, transfering money will use the built-in variable `Balance`.

## Built-in features

Here we have all the built-in variables and functions. This consists of the bare essentials for a Banking Management System --- e.g, Account Balance, ...

## Built-in variables ,function , classes

ran_16_card_num() = Function which makes a random credit card number (16 digits) with the 16th digit being a check digit which uses a wieghted sum MOD 10 to create it.

Base_Account = Base Class for all future types of accounts which has card_numbers,account_number and balance built in.

Simple_Account = Inherits from Base_Account but adds loans.
