# Banking Management System


## Architecture

The program shall have a menu listing all of its user-available functionality --- i.e., 
- Create Account, 
- Close Account, 
- Withdraw, 
- Tranfer, 
- Exit 
- ...

All files work around a **core system**: if one wants to transfer or withdraw, for example, they will need to call the **built-in variable** `Balance` and change it. Such built-in functionality serve as constants to which all the different files can refer and work their algorithms upon. Main.py --- the core system --- will simply call such functions.

Below is an example of the how Main.py relates to all other files which every one can implement their own.

```python
import CreateAccount
import CloseAccount
import Transfer
import Exit
import Withdraw


def Main():

  command = ""

  while True:
    if command == "Create Account": 
      CreateAccount()

    if command == "Close Account": 
      CloseAccount()

    if command == "Transfer": 
      Transfer()

    if command == "Exit": 
      Exit()  
  

if __name__ == "__main__":
  Main()
  
```




## Built-in features : variables, functions, classes

Here we is a list of all the built-in functionality which you can use in order to create your own file to be called by Main.py.


- `ran_16_card_num()` : Function which makes a random credit card number (16 digits) with the 16th digit being a check digit which uses a weighted sum MOD 10 to create it.

- `Base_Account`: Base Class for all future types of accounts which has card_numbers,account_number and balance built in.



## Ideas

- **Parser for command-line commands.**  (each a_k represents an account number)
  - `Merge(a1, a2, ...)` : Merges all accounts `a1, a2, ...` together --- i.e., unify all accounts by having only one Card Number, only one Balance consisting of their sum etc.
  - `Delete(a1, a2, ...)` : deletes all accounts `a1, a2, ...`
  - `CheckBalance(a)` : Checks the balance for the account `a`.
- ...
