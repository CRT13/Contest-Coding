    Copyright (c) 2018-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# CCpp (Scraps)

> Uncategorized C/C++ code snippets.

```c
/* [01a] C: Swap 2 numbers (with intermediate variable) */
#include <stdio.h>
main(){
	int x,y,z;
	printf("\nEnter 2 Numbers: ");
		scanf("%d %d",&x,&y);
	printf("\nOriginal Values: ");
		printf("X,Y = %d,%d",x,y);
	z=x;
	x=y;
	y=z;
	printf("Swapped Values: \n");
		printf("X,Y = %d,%d",x,y);
}
```


      File "<ipython-input-1-fb130be35beb>", line 1
        *(C:, Swap, 2, numbers, (with, intermediate, variable), */)
           ^
    SyntaxError: invalid syntax




```c
/* [01b] C: Swap 2 numbers (without intermediate variable, using arithmetic operations) */
#include <stdio.h>
main(){
	int x,y;
	printf("\nEnter 2 Numbers: ");
		scanf("%d %d",&x,&y);
	printf("\nOriginal Values: ");
		printf("X,Y = %d,%d",x,y);
	x = x+y;
	y = x-y;
	x = x-y;
	printf("\nSwapped Values: ");
		printf("X,Y = %d %d",x,y);
}
```


```c
/* [01c] C: Swap 2 numbers (without intermediate variable, using logical operations) */
#include <stdio.h>
main(){
	int x,y;
	printf("\nEnter 2 Numbers: ");
		scanf("%d %d",&x,&y);
	printf("\nOriginal Values: ");
		printf("X,Y = %d,%d",x,y);
	x = x^y;
	y = x^y;
	x = x^y;
	printf("\nSwapped Values: ");
		printf("X,Y = %d,%d",x,y);
}
```


```c
/* [02] C: Convert Celsius to Fahrenheit Scale */
#include <stdio.h>
main(){
	float celsius,fahrenheit;
	printf("Enter temperature (*C): ");
		scanf("%f",&celsius);
	fahrenheit = 1.8 * celsius + 32;
	printf("Temperature (*C): %f",celsius);
	printf("Temperature (*F): %f",fahrenheit);
}
```


```c
/* [03a] C: Convert a complex number from rectangular to polar form */
#include <stdio.h>
#include <math.h>
#define PI 3.1415927
main(){
	// Assume z = x + iy = r(cis(k)) form
	float x,y,magnitude,angle=0.0;
	printf("Enter real/imaginary values => z=(x,y): ");
		scanf("%f,%f",&x,&y);
	magnitude = sqrt((x*x)+(y*y));
	if ((x>0) && (y>0))			angle = (atan(y/x) * (180/PI));
	else if ((x<0) && (y>0))	angle = (atan(y/x) * (180/PI)) + 180.0;
	else if ((x<0) && (y<0))	angle = (atan(y/x) * (180/PI)) - 180.0;
	else if ((x>0) && (y<0))	angle = (atan(y/x) * (180/PI));
	else if ((x==0) && (y>0))	angle = +90.0;
	else if ((x==0) && (y<0))	angle = -90.0;
	printf("Rectangular Form => z = (x,y) = (%f,%f)",x,y);
	printf("Polar Form => z = (r,k) = (%f,%f)",magnitude,angle);
}
```


```c
/* [03b] C: Convert a complex number from polar to rectangular form */
#include <stdio.h>
#include <math.h>
#define PI 3.1415927
main(){
	// Assume z = x + iy = r(cis(k)) form
	float x,y,magnitude,angle=0.0;
	printf("Enter real/imaginary values => z=(r,k): ");
		scanf("%f,%f",&magnitude,&angle);
	x = (magnitude * (cos((angle*PI)/180)));
	y = (magnitude * (sin((angle*PI)/180)));
	printf("Polar Form => z = (r,k) = (%f,%f)",magnitude,angle);
	printf("Rectangular Form => z = (x,y) = (%f,%f)",x,y);
}
```


```c
/* [04a] C: Find maximum/minimum of 3 numbers (using IF statements) */
#include <stdio.h>
main(){
	float x,y,z,max;
	printf("Enter 3 numbers (x,y,z): ");
		scanf("%f,%f,%f",&x,&y,&z);
	max = min = x;
	// MAX steps
	if(y>max)	max=y;
	if(z>max)	max=z;
	// MIN steps
	if(y<min)	min=y;
	if(z<min)	min=z
	printf("MAX(x,y,z), MIN(x,y,z) = %f, %f",max,min);
}
```


```c
/* [04b] C: Find maximum/minimum of 3 numbers () */
```


```c
/* [05] C: Find if number is even/odd */
#include <stdio.h>
main(){
	int n;
	printf("Enter number (n): ");
		scanf("%d",&n);
	if(n%2 == 0)	printf("Even");
	else			printf("Odd");
}
```


```c
/* [06] C: Find if number is even/odd */
#include <stdio.h>
main(){
	int n;
	printf("Enter number (n): ");
		scanf("%d",&n);
	if(n%2 == 0)	printf("Even");
	else			printf("Odd");
}
```


```c
/* [07a] C: Find if number is prime/composite */
#include <stdio.h>
main(){

}
```


```c
/* [07b] C: Find if number is perfect cube */
#include <stdio.h>
main(){

}
```


```c
/* [08] C: Compute simple & compound interest */
#include <stdio.h>
main(){
/*
		P = Principal
		R = Rate of Interest
		N = Duration (years)
		A = Amount
		SI = Simple interest
		CI = Compound interest
*/
	float P,R,N,A,SI,CI;
	printf("Enter (Principal,Rate-of-interest,Duration): ");
		scanf("%f,%f,%f",&P,&R,&N);
	SI = (P*R*N)/100;
	A = P * pow((double)(1+r/100), (double)(n));
	CI = A-P;
	printf("Simple/Compound interests are => (SI,CI) = (%.2f,%.2f)",SI,CI);
}
```


```c
/* [09] C: Find if given year is a leap year */
#include <stdio.h>
main(){
	int year;
	printf("Enter the Year: ");
		scanf("%d",&year);
	if ((year%4 == 0) && ((year%100 == 0) || (year%400 != 0)))
		printf("Leap Year");
	else
		printf("Not a Leap Year");
}
```


```c
/* [0Aa] C: Find if a number is a power of 2 */
#include <stdio.h>
#include <math.h>
main(){
	long int n;
	printf("Input: ");
		scanf("%li",&n);
	if (ceil(log2(n)) == floor(log2(n)))
		printf("Power of 2");
	else
		printf("Not a power of 2");
}
```


```c
/* [0B] C: Find the number of occurrences of a digit in an integer numeral */
#include <stdio.h>
main(){
	int digit,count=0,remainder;
	long int n;
	printf("Enter Number & Digit (n d): ");
		scanf("%li %d",&n,&digit);
  while(n!=0){
	remainder = n%10;
	if(remainder==digit)	count++;
	n /= 10;
  }
  printf("\nThe occurrence of %d is %d times",digit,count);
}
```


#### 01. C Program without main(): ([reference](https://www.geeksforgeeks.org/write-running-c-code-without-main/)) ||| [source](#cell01)
    C programs without explicit declaration of main() function.
#### 02. Preprocessor Directives: ([reference](https://www.geeksforgeeks.org/interesting-facts-preprocessors-c/)) ||| [source](#cell02)
    Ideas for pre-processor directive usage.
#### *. Template: ([reference]( )) ||| [source](#cell03)
    Template Element.

<a id="cell01"></a>

### 01. C Program without main()


```python
/* [1]: Using a macro that defines main() */
#include <stdio.h>
#define f1 main

int f1(){
    printf("Hello World");
    return 0;
}
```


```python
/* [2]: Using token-pasting operator to define main() */

#include <stdio.h>
#define f2 m##a##i##n

int f2(){
    printf("Hello World");
    return 0;
}
```


```python
/* [3]: Using argumented macro to define main() */
#include <stdio.h>
#define f3(m,a,i,n) m##a##i##n
#define start f3(m,a,i,n)

int start(){
    printf("Hello World");
}
```


```python
/* [4]: Using entry-point modification at compile-time */
/*
Usage:
    gcc filename.c -nostartfiles
*/
#include <stdio.h>
#include <stdlib.h>

int f4();

int _start(){
    f4();
    exit(0);
}
int f4(){
    puts("Hello World");
}
```

<a id="cell02"></a>

### 02. Pre-Processor Directives

##### 1. Defining a Constant


```python
#include <stdio.h>
#define PI 3.14

main(){
    printf("Pi = %f",PI);
}
```

##### 2. Increment/Decrement Operators


```python
#include <stdio.h>
#define inc(x) ++x
#define dec(x) --x

main(){
    char *ptr = "Hello World";
    int x = 13;
    printf("\n%s\n%d",inc(ptr),inc(x));
    printf("\n%s\n%d",dec(ptr),dec(x));
}
```

##### 3. Macro arguments are not evaluated before Macro Expansions


```python
#include <stdio.h>
#define add(x,y) (x+y)
#define sub(x,y) (x-y)
#define mul(x,y) (x*y)
#define div(x,y) (x/y)
#define mod(x,y) (x%y)

main(){
    int x=2,y=3;
    printf("\nADD=%d,\nSUB=%d,\nMUL=%d,\nDIV=%d,\nMOD=%d",
            add(x+2,y+1),sub(x+2,y+1),mul(x+2,y+1),div(x+2,y+1),mod(x+2,y+1));

}
```

##### 4. Token-Pasting Operator


```python
#include <stdio.h>
#define merge(x,y) x##y

main(){
    printf("%d",merge(12,34));
}
```

##### 5. A token passed to a macro can be converted to string literal using '#'


```python
#include <stdio.h>
#define to_string(x) #x

main(){
    printf("%s",to_string(Hello World));
}
```

##### 6. Standard Macros


```python
#include <stdio.h>

main(){
    printf("\nCurrent File: %s",__FILE__);
    printf("\nC Version: %s",__STDC_VERSION__);
    printf("\nCurrent Date: %s",__DATE__);
    printf("\nCurrent Time: %s",__TIME__);
    printf("\nCurrent Line: %s",__LINE__);
}
```
