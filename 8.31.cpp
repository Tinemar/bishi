#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int numofpeople(int n,int k,vector<int> s){
    if (s.size()==0){
        return 0;
    }
    int result = 0;
    sort(s.begin(),s.end());
    // for(int i=0;i<s.size();++i){
    //     for(int j=1;j<s.size();++j){
    //         if (s[j]-s[i]<=k){
    //             result += 1;
    //         }
    //         else{
    //             break;
    //         }
    //     }
    // }
    int start = 1;
    for(int i=start;i<s.size();++i){
        if(s[i]-s[i-1]<=k){
            result ++;
        }
    }
    return result;
}
int main(){
    int n,k;
    cin>>n>>k;
    vector<int> s;
    int a;
    for(int i=0;i<n;++i){
        cin>>a;
        s.push_back(a);
    }
    cout<<numofpeople(n,k,s)<<endl;
    return 0;
}