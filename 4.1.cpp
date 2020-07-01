#include<iostream>
using namespace std;
double SqrtByNewton(const double& _val)
{
    double nrt = _val ; 
    double last_nrt = 0 ;
     while (nrt != last_nrt)
     {
         last_nrt = nrt ;
         nrt = (nrt + _val / nrt) / 2.0 ;
     }
     return  nrt ;
}
int main(){
    double result = SqrtByNewton(12.2);
    cout<<result<<endl;
    return 0;
}