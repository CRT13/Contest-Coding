    Copyright (c) 2018-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# Python3 (Scraps)

> Uncategorized Python3 code snippets.

### Index:
#### 01. Dictionaries: ([reference]( )) ||| [source](#cell01)
#### 02. repr() v/s str(): ([reference]( )) ||| [source](#cell02)
#### 03. Return the product of a list: ([reference]( )) ||| [source](#cell03)
    Determine fastest way to return product of list elements.
#### 04. Find common list elements: ([reference]( )) ||| [source](#cell04)
#### 05. Delete common list elements: ([reference]( )) ||| [source](#cell05)
#### 06. Delete duplicate list elements: ([reference](https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6)) ||| [source](#cell06)
    Determine fastest way to remove duplicate elements in a list while maintaining order.

```python
""" Python3: Scrap all hyperlinks from a webpage """
from urllib.request import urlopen
import re

url = "https://sites.google.com/site/s4p2018daiict/committee"
# url =
website = urlopen(url)
html = website.read().decode('utf-8')
links = re.findall('"((http|ftp)s?://.*?)"', html)

print(*list(set([i[0] for i in links])),sep='\n')
```

### * Dictionaries


```python
A = {'jack': 4098, 'sape': 4139,'guido': 4127}

# Return list of keys - Unsorted/Sorted
print(list(A))
print(sorted(A))

# Check if key exists
print('guido' in A,'sape' not in A)

# Create dictionary directly from (key,value) pairs
B = dict([('sape',4139),('guido',4127),('jack',4098)]);print(B)
# Create dictionary directly by key=value assignments (when keys are simple strings)
C = dict(sape=4139,guido=4127,jack=4098);print(C)
k1,k2,k3 = 'sape','guido','jack'
C2 = dict(k1=4139,k2=4127,k3=4098);print(C2)
# Create dictionary using dict-comprehension
D = {x: x**2 for x in range(10)};print(D)
# Create dictonary using zip()
E1 = [i for i in range(10)];print(E1)
# E2 = [j for j in 2**range(10)]
# E = dict(zip(E1,E2))
```

    ['jack', 'sape', 'guido']
    ['guido', 'jack', 'sape']
    True False
    {'sape': 4139, 'guido': 4127, 'jack': 4098}
    {'sape': 4139, 'guido': 4127, 'jack': 4098}
    {'k1': 4139, 'k2': 4127, 'k3': 4098}
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
# a-e are five ways of creating the same dictionary
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e
```




    True




```python
# Retrieve key,value pair
for key,value in A.items():
    print(key,value,sep='->')
# Retrieve index,value of a key
for index,value in enumerate(A):
    print(index,value,sep='->')
# Loop over 2+ sequences simultaneously
A1 = dict(sape=4139,guido=4127,jack=4098)
A2 = dict(james=8339,alex=2137,tom=4978)
for i,j in zip(A1.items(),A2.items()):
    print(i,j,sep='->',end=' ')
```

    ['jack', 'sape', 'guido']
    ['guido', 'jack', 'sape']
    True False
    {'sape': 4139, 'guido': 4127, 'jack': 4098}
    {'sape': 4139, 'guido': 4127, 'jack': 4098}
    {'k1': 4139, 'k2': 4127, 'k3': 4098}
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    jack->4098
    sape->4139
    guido->4127
    0->jack
    1->sape
    2->guido



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-23-875fe028cc2b> in <module>()
         26 A1 = dict(sape=4139,guido=4127,jack=4098)
         27 A2 = dict(james=8339,alex=2137,tom=4978)
    ---> 28 for i,j in zip(A1.items()[0],A2.items()[0]):
         29     print(i,j,sep='->',end=' ')


    TypeError: 'dict_items' object does not support indexing


<a id="cell02"></a>


### * repr() v/s str()
    repr() gives the formal representation,
    str() gives the informal representation.


```python
import datetime
now = datetime.datetime.now()
print(str(now),repr(now),sep='\n')
```

    2018-06-27 01:21:24.289492
    datetime.datetime(2018, 6, 27, 1, 21, 24, 289492)



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


<a id="cell03"></a>

### * Return the product of a list
    np.prod() evaluates the fastest


```python
# Calculate n!
from operator import mul
from functools import reduce

n = 10
X = [x for x in range(1,n+1)]
print(reduce(mul,X,1))
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    3628800



```python
# Timing Evaluation
from operator import mul
from functools import reduce
import numpy as np
import numexpr as ne

r = range(1,101)
%timeit reduce(lambda x,y: x*y,r)
%timeit reduce(mul,r)
%timeit np.prod(r)
%timeit ne.evaluate("prod(r)")
```

    61.2 µs ± 5.01 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    35.3 µs ± 2.44 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    62.9 µs ± 2.43 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    88.9 µs ± 3.03 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)



```python
# Timing Evaluation
from operator import mul
from functools import reduce
import numpy as np
import numexpr as ne

R = [range(1,101),np.array(range(1,101)),\
     np.arange(1,1e4,dtype=int),\
     np.arange(1,1e5,dtype=float)]
for r in R:
    %timeit reduce(lambda x,y: x*y,r)
    %timeit reduce(mul,r)
    %timeit np.prod(r)
    %timeit ne.evaluate("prod(r)")
```

    56.3 µs ± 933 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    32.1 µs ± 431 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    63.2 µs ± 2.87 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    87.6 µs ± 2.37 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)


    C:\Users\Satellite\AppData\Roaming\Python\Python36\site-packages\ipykernel_launcher.py:1: RuntimeWarning: overflow encountered in long_scalars
      """Entry point for launching an IPython kernel.


    211 µs ± 23.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)


    C:\Users\Satellite\AppData\Roaming\Python\Python36\site-packages\ipykernel_launcher.py:1: RuntimeWarning: overflow encountered in long_scalars
      """Entry point for launching an IPython kernel.


    179 µs ± 5.75 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    9.42 µs ± 236 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    36.5 µs ± 210 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)


    C:\Users\Satellite\AppData\Roaming\Python\Python36\site-packages\ipykernel_launcher.py:1: RuntimeWarning: overflow encountered in long_scalars
      """Entry point for launching an IPython kernel.


    7.09 ms ± 244 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


    C:\Users\Satellite\AppData\Roaming\Python\Python36\site-packages\ipykernel_launcher.py:1: RuntimeWarning: overflow encountered in long_scalars
      """Entry point for launching an IPython kernel.


    4.95 ms ± 257 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    50 µs ± 1.46 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    162 µs ± 4.96 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)


    C:\Users\Satellite\AppData\Roaming\Python\Python36\site-packages\ipykernel_launcher.py:1: RuntimeWarning: overflow encountered in double_scalars
      """Entry point for launching an IPython kernel.


    74.3 ms ± 3.89 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)


    C:\Users\Satellite\AppData\Roaming\Python\Python36\site-packages\ipykernel_launcher.py:1: RuntimeWarning: overflow encountered in double_scalars
      """Entry point for launching an IPython kernel.


    48.4 ms ± 2.82 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)


    C:\Users\Satellite\AppData\Roaming\Python\Python36\site-packages\numpy\core\_methods.py:35: RuntimeWarning: overflow encountered in reduce
      return umr_prod(a, axis, dtype, out, keepdims)


    702 µs ± 101 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
    1.44 ms ± 149 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)


<a id="cell04"></a>

### * Find Common List Elements


```python
a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]

c = ['XS','XS','M']
d = ['XL','S','XS']

# When order is insignificant
print(set(a) & set(b),(set(c) & set(d)))
# When order is significant
print([i for i,j in zip(a,b) if i == j],[i for i,j in zip(c,d) if i == j])
```

    {5} {'XS'}
    [5] []


<a id="cell05"></a>

### * Delete Common List Elements


```python
a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]

c = ['XS','XS','M']
d = ['XL','S','XS']

# When order is insignificant
print(list(set(a)^set(b)),list(set(c)^set(d)))
# When order is significant
```

    [1, 2, 3, 4, 6, 7, 8, 9] ['XL', 'S', 'M']


<a id="cell06"></a>

### * Delete Duplicate List Elements


```python
def f1():
    hash = {}
    [hash_.__setitem__(x, 1) for x in seq]
    return hash_.keys()
def f2():
def f3a():
def f3b():
def f4():
def f5():
def f6():
def f7():
def f8():
def f9():


```

### * [Split list into sublists](https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists)

    chunks = [data[x:x+100] for x in range(0, len(data), 100)]
