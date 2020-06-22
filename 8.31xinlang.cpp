#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
// int numofpeople(int n,int k,vector<int> s){
//     if(s.size()==0){
//         return 0;
//     }
//     int result = 0;
//     sort(s.begin(),s.end());
//     int start = 0;
//     int end = 1;
//     for(start<end && end<s.size()){
//         if(s[end]-s[start]<=k){
//             result ++;
//             start = end+1;
//             end = start + 1;
//         }
//         else{
//             start = end;
//             end = end+1;
//         }
//     }
//     return result;
// }
// int main(){
//     int n,k;
//     cin>>n>>k;
//     vector<int> s;
//     int a;
//     for(int i=0;i<n;++i){
//         cin>>a;
//         s.push_back(a);
//     }
//     cout<<numofpeople(n,k,s)<<endl;
//     return 0;
// }
int output(int n,int m,int k,vector<int> s){
    int maxsum = 0;
    int index = 0;
    int cursum = 0;
    
    return maxsum;
}
int mian(){
    int n,m,k;
    cin>>n>>m>>k;
    vector<int> s;
    int a;
    for(int i=0;i<n;++i){
        cin>>a;
        s.push_back(a);
    }

}