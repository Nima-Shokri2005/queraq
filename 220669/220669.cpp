#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
  int n;
  cin >> n;
  string res;
  for(int i = 0; i < n - 1; i++)
  {
    string tmp;
    for (int j = 0; j < ((2 * n) - 1); j++)
    {
      if(j != (n) - (i + 1) and j != (n - 1) + (i))
      {
        tmp += '.';
      }
      else
      {
        tmp += 'D';
      }
    }
    res += tmp + '\n';
  }
for (int i = 0; i < ((2 * n) - 1); i++)
{
  if(i % 2 == 0)
    res += 'D';
  else
    res += '.';
}
cout << res;

  
}