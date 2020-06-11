/* C: Use named operators */
#include <stdio.h>
#include <iso646.h>
main(){
    int A = 0b1010;
    int B = 0b0101;
    printf("%0x %d %d %d",
        compl A,
        A bitand B,
        A bitor B,
        A xor B
    );
}