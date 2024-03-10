#include <iostream>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    if(c==0 && d==0)
    {
        cout<<"0";
        exit(0);
    }
    if((c+d)%(a*b)==0)
    {
        cout<<a*b;
        exit(0);
    }
    cout<<(c+d)%(a*b);
}