#include<iostream>
#include<vector>
using namespace std;
int maxSubString(vector<int> &arr,int &begin,int &end){
    int maxSum = 0;
    int curSum = 0;
    int index = 0;
    for(int i=0;i<arr.size();++i){
        curSum += arr[i];
        if(curSum<0){
            index = i+1;
            curSum = 0;
        }
        if(curSum>maxSum){
            maxSum = curSum;
            begin = index;
            end = i;
        }
    }
    return maxSum;
}
int main(){
    int len;
    cin>>len;
    vector<int> arr;
    int a;
    for(int i=0;i<len;++i){
        cin>>a;
        arr.push_back(a);
    }
    int begin,end;
    maxSubString(arr,begin,end);
    for(int i=begin;i<=end;++i){
        cout<<arr[i]<<endl;
    }
    return 0;
}