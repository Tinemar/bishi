#include<algorithm>
#include<iostream>
#include<cstdio>
using namespace std;
long long n,m,sum,ans,a[2000001];      //都打成ll保险！        
int main()
{
    scanf("%lld%lld",&n,&m);
    for(int i=1;i<=n;++i)
    scanf("%lld",&a[i]);
    a[n+1]=m;                   
    sort(a+1,a+1+n+1);            
    if(a[1]!=1)//排序后没有1？骗谁，连1都表示不出来了，没答案！                 
    {
        printf("No answer!!!\n");   
        return 0;     
    }
    for(int i=1;i<=n;++i)
    {
        while(sum<a[i+1]-1) //贪心的思想        
        {
            sum+=a[i];
            ans++;           
            if(sum>=m)
            {
                printf("%lld\n",ans);  
                return 0;
            }
        }   
    }
    printf("%lld\n",ans+1);
    return 0;
}