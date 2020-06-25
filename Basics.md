    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# Basic Problems

> Personal solutions to programming puzzles/challenges.

# Index

| Problem | PowerShell | Python3 | C/C++ | JS |
| :-- | :--: | :--: | :--: | :--: |
| [Bit Operations](#bit-operations) |  | ✔️ | ✔️ |  |
| [100 Doors](#100-doors) | ✔️ | ✔️ | ✔️ | ✔️ |

### Bit Operations

Refer: [Problem](http://www.rosettacode.org/wiki/Bitwise_operations) <br>

```c
# /* C: Bit-wise Operations */

void bitwise(int a, int b){
  printf("a and b: %d\n", a & b);
  printf("a or b: %d\n", a | b);
  printf("a xor b: %d\n", a ^ b);
  printf("not a: %d\n", ~a);
  printf("a << n: %d\n", a << b); /* left shift */
  printf("a >> n: %d\n", a >> b); /* on most platforms: arithmetic right shift */
  /* convert the signed integer into unsigned, so it will perform logical shift */
  unsigned int c = a;
  printf("c >> b: %d\n", c >> b); /* logical right shift */
  /* there are no rotation operators in C */
  return 0;
}
/* rotate x to the right by s bits */
unsigned int rotr(unsigned int x, unsigned int s){
    return (x >> s) | (x << 32 - s);
}
```

```cpp
/* C++: Bit-wise Operations */

#include <iostream>
using namespace std;

void bitwise(int a, int b){
    cout << "a and b: " << (a & b)  << '\n'; // Note: parentheses are needed because & has lower precedence than <<
    cout << "a or b:  " << (a | b)  << '\n';
    cout << "a xor b: " << (a ^ b)  << '\n';
    cout << "not a:   " << ~a       << '\n';
    cout << "a shl b: " << (a << b) << '\n'; // Note: "<<" is used both for output and for left shift
    cout << "a shr b: " << (a >> b) << '\n'; // typically arithmetic right shift, but not guaranteed
    unsigned int c = a;
    cout << "c sra b: " << (c >> b) << '\n'; // logical right shift (guaranteed)
    // there are no rotation operators in C++
}
```

```python
""" Python3: Bit-wise Operations """

# class BitOperations(self,a,b):
#   def __init__():
#       self.a = a
#       self.b = b
#   def _not():
#       return(~self.a)
#   def _and():
#       return(self.a & self.b)
#   def _or():
#       return(self.a | self.b)
#   def nand():
#       return(~(self.a & self.b))
#   def nor():
#       return(~(self.a & self.b))
#   def xor():
#       return(self.a ^ self.b)
#   def xnor():
#       return(~(self.a ^ self.b))
#   def lshift():
#       return(a<<b)
#   def rshift():
#       return(a>>b)
operators = ['NOT','AND','OR',
             'NAND','NOR','XOR','XNOR',
             '<<','>>']
a,b = input().split(' ',maxsplit=1)
a,b = int(a),int(b)
# Aliter: assign datatype int, float, ... based on input. But how?
# Apply a,b to each method of BitOperations class
# Map result with bit_operations, and print it.
for operator in operators:
    print('A {} B = '.format(operator))
#     print('A {} B = {}'.format(operator,operation(a,b)))
```

### 100 Doors

Refer: [Problem](https://rosettacode.org/wiki/100_doors) <br>

The number of times a door is toggled is equal to it's number of unique factors. <br>
eg. Door #20 will be toggled 6 times (1,2,4,5,10,20) <br>
Each pair of toggles will put the door in it's initial state (CLOSED). <br>
The only numbers that will have odd number of factors are perfect squares (they have a repeated factor). <br>
So, the only doors to be OPEN in the end will be perfect squares. (1,4,9..100) <br>

```powershell
1..10 | forEach {"Door $($_*$_) is open!"}
```
```python
for i in range(1,11):
    print(f"Door {i**2} is open!")
```
```c
for (int i=1; i < 11; i++)
    printf("\nDoor %d is open!", i*i);
```
```js
for (var i=1; i<11; i++)
    console.log(`Door ${i*i} is open!`);
```

