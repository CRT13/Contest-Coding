    Copyright (c) 2018-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# CodeChef - Contest Problems

> Personal solutions to programming puzzles/challenges.


## Beginner

* [ATM](https://www.codechef.com/problems/HS08TEST)

* [Enormous Input Test](https://www.codechef.com/problems/INTEST)

* [Factorial](https://www.codechef.com/problems/FCTRL)

* [Small factorials](https://www.codechef.com/problems/FCTRL2)

* [Turbo Sort](https://www.codechef.com/problems/TSORT)

* [The Lead Game](https://www.codechef.com/problems/TLG)

* [Add Two Numbers](https://www.codechef.com/problems/FLOW001)

* [Find Remainder](https://www.codechef.com/problems/FLOW002)


```python
# [1: Input & Output simultaneously]
t = int(input())
while(t>0):
    a,b = input().strip().split()
    a,b = (int(a),int(b))
    print(a%b)
    t-=1
```

    3
    1 2
    1
    100 200
    100
    10 40
    10



```python
# [2: Input first, Output later]
Y = []
t = int(input())
while(t>0):
    a,b = input().strip().split()
    a,b = (int(a),int(b))
    Y.append(a%b)
    t-=1
print(*Y,sep='\n')
```

    3
    1 2
    100 200
    10 40
    1
    100
    10


* [](https://www.codechef.com/problems/FLOW003)

* [First and Last Digit](https://www.codechef.com/problems/FLOW004)

* [Smallest Numbers of Notes](https://www.codechef.com/problems/FLOW005)

* [Sum of Digits](https://www.codechef.com/problems/FLOW006)

* [Reverse The Number](https://www.codechef.com/problems/FLOW007)

* [Servant](https://www.codechef.com/problems/FLOW008)

* [Total Expenses](https://www.codechef.com/problems/FLOW009)

* [Id and Ship](https://www.codechef.com/problems/FLOW010)

* [Gross Salary](https://www.codechef.com/problems/FLOW011)

* [](https://www.codechef.com/problems/FLOW012)

* [Valid Triangles](https://www.codechef.com/problems/FLOW013)

* [Grade The Steel](https://www.codechef.com/problems/FLOW014)

* [Gregorian Calendar](https://www.codechef.com/problems/FLOW015)

* [GCD and LCM](https://www.codechef.com/problems/FLOW016)

* [Second Largest](https://www.codechef.com/problems/FLOW017)

* [Small Factorial](https://www.codechef.com/problems/FLOW018)


```python
class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    """ Returns formal representation """
    def __repr__(self):
        return 'Rational(%s,%s)'%(self.real,self.imag)
    """ Returns informal representation """
    def __str__(self):
        return '%s + i%s'%(self.real,self.imag)
z = Complex(2,7)
print(str(z),repr(z),sep='\n')
```

    2 + i7
    Rational(2,7)


# CodeChef - Challenges

## Division 2

### [June (10-day)](https://www.codechef.com/JUNE18B)

* [Naive Chef](https://www.codechef.com/JUNE18B/problems/NAICHEF)

* [Binary Shuffle](https://www.codechef.com/JUNE18B/problems/BINSHFFL)

* [Vision](https://www.codechef.com/JUNE18B/problems/VSN)

* [Sheokand and String](https://www.codechef.com/JUNE18B/problems/SHKSTR)

* [Two Flowers](https://www.codechef.com/JUNE18B/problems/TWOFL)

* [Ways to Work](https://www.codechef.com/JUNE18B/problems/WRKWAYS)

* [Expected Buildings](https://www.codechef.com/JUNE18B/problems/BUILDIT)

* [Warehouseman](https://www.codechef.com/JUNE18B/problems/WAREHOUS)

### [July (10-day)](https://www.codechef.com/JULY18B)

* [Naive Chef](https://www.codechef.com/JUNE18B/problems/NAICHEF)


```python
#!/usr/bin/python3
""" Python3: https://www.codechef.com/problems/HS08TEST """
import sys

# sys.stdin() = open('input.txt'','r')

x,y = [float(i) for i in sys.stdin.read().split()]  # Transaction,Balance Amounts
if x+0.5 <= y and int(x)%5 == 0:
    y -= x+0.5
print('%.2f' %y)
```


      File "<ipython-input-1-0679e4d6b441>", line 5
        sys.stdin() = open('input.txt'','r')
                                            ^
    SyntaxError: EOL while scanning string literal


