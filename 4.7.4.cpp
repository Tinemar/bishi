#include <iostream>
#include <vector>
#include<deque>
#include <string>
#include<algorithm>
using namespace std;
vector<int> com1(deque<int> num,int N){
    vector<int> result;
    result.push_back(num[0]);
    num.erase(num.begin());
    while(!num.empty() && !result.empty()){
        int temp = result.back();
        if(abs(temp-num[0])>abs(temp-num[num.size()-1])){
            result.push_back(num[0]);
            num.erase(num.begin());
        }
        else{
            result.push_back(num[num.size()-1]);
            num.erase(num.end());
        }
    }
    return result;
}
vector<int> com2(deque<int> num,int N){
    vector<int> result;
    result.push_back(num[N-1]);
    num.erase(num.end());
    while(!num.empty() && !result.empty()){
        int temp = result.back();
        if(abs(temp-num[0])>abs(temp-num[num.size()-1])){
            result.push_back(num[0]);
            num.erase(num.begin());
        }
        else{
            result.push_back(num[num.size()-1]);
            num.erase(num.end());
        }
    }
    return result;
}
int main()
{
    int N;
    cin >> N;
    if(N==0)
        return 0;
    string nums;
    deque<int> num;
    for(int i=0;i<2;++i)
    {
        getline(cin, nums);
        for (int i = 0; i < nums.size(); i += 2)
        {
            num.push_back(nums[i] - '0');
        }
    }
    vector<int> result = com1(num,N);
    vector<int> result2 = com2(num,N);
    int res,res2=0;
    for(int i=1;i<N;++i){
        res += abs(result[i]-result[i-1]);
    }
    for(int i=1;i<N;++i){
        res2 += abs(result2[i]-result2[i-1]);
    }
    (res>res2)?(cout<<res):(cout<<res2);
    return 0;
}