#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main()
{
    long long int n,a,b,min;
    cin>>a>>b;
    min=a;
    if(b<min)
        min=b;
    cout<<min;
    return 0;
}