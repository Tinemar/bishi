#include <iostream>
#include <algorithm>
#include <vector>
#include<map>
using namespace std;
vector<int> FindMin(int money,vector<int> coin, int n)
{
	int *coinNum=new int[money+1]();
	int *coinValue=new int[money+1]();
	coinNum[0]=0;
 
	for(int i=1;i<=money;i++)
	{
		int minNum=i;
		int usedMoney=0;
		for(int j=0;j<n;j++)
		{
			if(i>=coin[j])
			{
				if(coinNum[i-coin[j]]+1<=minNum&&(i==coin[j]||coinValue[i-coin[j]]!=0))
				{
					minNum=coinNum[i-coin[j]]+1;
					usedMoney=coin[j];
				}
			}
		}
		coinNum[i]=minNum;
		coinValue[i]=usedMoney;
	}
    vector<int> moneys;
	if(coinValue[money]==0)
		return moneys;
	else
	{
		while(money>0)
		{
			moneys.push_back(coinValue[money]);
			money-=coinValue[money];
		}
		return moneys;
	}
	delete []coinNum;
	delete []coinValue;
}
int main() {
    int m;
    int n;
    cin>>m>>n;
    vector<int> value;
    for(int i=n;i>0;i--){
        int temp;
        cin>>temp;
        value.push_back(temp);
    }
    map<int,int> res;
    for(int i=1;i<=m;++i){
        vector<int> moneys = FindMin(i,value,n);
        map<int,int> m;
        for(vector<int>::iterator iter = moneys.begin();iter!=moneys.end();++iter){
            if(m.count(*iter)){
                m[*iter]+=1;
            }
            else{
                m.insert(pair<int,int>(*iter,1));
            }
        }
        for(map<int,int>::iterator iter = m.begin();iter!=m.end();++iter){
            if(!res.count(iter->first))
            {
                res.insert(pair<int,int>(iter->first,iter->second));
            }
            else if(res.count(iter->first)&&res[iter->first]<iter->second)
                res[iter->first] = iter->second;
        }
    }
    int result = 0;
    //todo 去掉能够重复计算的值
    for(map<int,int>::iterator iter=res.begin();iter!=res.end();++iter){
        result += res[iter->first];
    }
    cout<<result<<endl;
    return 0;
}