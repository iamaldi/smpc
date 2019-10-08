# Secure Summation

This project represents an implementation of Secure Summation with n Parties.


## Install

#### Prerequisites
You can run this program using either Python 2 or Python 3.

Clone this repository
```console
$ git clone https://github.com/iamaldi/smpc
```
## Usage
Change directory to ```smpc/```
```console
$ cd smpc/
```
Execute ```sec_sum.py```
```console
$ python3 sec_sum.py

How many Parties would you like to create: 4

------------------------- Creating 4 Parties -------------------------

Enter a secret value for Party_0: 10
Enter a secret value for Party_1: 11
Enter a secret value for Party_2: 20
Enter a secret value for Party_3: 20

------------------------- Computing Common Function f(x) -------------------------

Party_0 has computed f(x) = 61
Party_1 has computed f(x) = 61
Party_2 has computed f(x) = 61
Party_3 has computed f(x) = 61

```