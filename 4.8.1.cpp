#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int main(){
    string ListNode;
    getline(cin,ListNode);
    vector<char> List;
    string res = "false";
    for(int i=0;i<ListNode.size();i+=2){
        if(count(List.begin(),List.end(),ListNode[i])>0){
            res = "true";
            break;
        }
        List.push_back(ListNode[i]);
    }
    cout<<res;
    return 0;
}