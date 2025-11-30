#include <iostream>
using namespace std;
int main() {
    float x,y,a;
    for(x=-1.5;x<1.5;x+=0.05) {
        a=x*x+y*y-1;
        char he = a*a*a-x*x*y*y*y<=0.7?'*':' ';
        cout << he;
        
        putchar('\n');
    }

    printf("i love you <3");
    return 0;
}