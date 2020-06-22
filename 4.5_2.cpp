#include <iostream>
#include <algorithm>
#include <vector>
#include<string>
#include<istream>
using namespace std;
int main(){
    int input[2];
    cin>>input[0]>>input[1];
    int n =input[0];
    string nums = to_string(input[1]);
    int zero_num =0;
    int one_num = 0;
    for(int i=0;i<nums.size();++i){
        if(nums[i] == '0')
            zero_num+=1;
        if(nums[i]=='1')
            one_num+=1;
    }
    cout<<abs(zero_num-one_num)<<endl;
    return 0;
}