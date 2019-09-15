Banking Management System

TODO: Design its architecture


## Architecture

Every one of us shall choose a functionality each of us will program. 

The program shall have a menu listing all of its user-available functionality --- i.e., Create Account, Close Account, Withdraw, Tranfer, Exit etc. Main.py will simply call such functions --- the implementation of such features entirely rely on every one of us. Here's an example of how Main.py works together with the files we shall implement:

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


All such features work around a **core system**: if one wants to transfer or withdraw, for example, they will need to call the **built-in variable** `Balance` and change it. Such built-in functionality serve as constants to which all the different files can refer and work their algorithms upon.

## Built-in features : variables, functions, classes

Here we have all the built-in variables and functions. This consists of the bare essentials for a Banking Management System --- e.g, Account Balance, ...


- `ran_16_card_num()` = Function which makes a random credit card number (16 digits) with the 16th digit being a check digit which uses a weighted sum MOD 10 to create it.

- `Base_Account`: Base Class for all future types of accounts which has card_numbers,account_number and balance built in.



## Ideas

- **Parser for commands.**  (each a_k represents an account number)
  - Merge(a1, a2, ...)
  - Delete(a1, a2, ...)
  - CheckBalance(a)

