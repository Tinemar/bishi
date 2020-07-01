#include<iostream>
#include <iomanip>
#include<vector>
#include<string>
#include<algorithm>
#include <sstream>

using namespace std;
struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
 };
ListNode* reverseKGroup(ListNode* head, int K) {
        if(!head || K <= 1) return head;
        int n = K;
        ListNode* cur = head;
        while(n--){
            if(!cur) return head;
            cur = cur->next;
        }
        ListNode *p1 = reverseKGroup(cur, K), *p2 = head, *p3 = head;
        while(K--){
            p3 = p2->next;
            p2->next = p1;
            p1 = p2;
            p2 = p3;
        }
        return p1;
    }
int main(){
    string sListNode;
    int K;
    vector<int> nums;
    for(int i=0;i<2;++i){
        if(i==0){
            getline(cin,sListNode);
            sListNode = sListNode.substr(1,sListNode.size()-1);
            cout<<sListNode;
            string temp;
            stringstream input(sListNode);
            while(getline(input,temp,','))
                nums.push_back(stoi(temp));
        }
        if(i==1){
            cin>>K;
        }
    }
    ListNode* pHead = new ListNode(0);
    ListNode* node = pHead;
    for(int i=0;i<nums.size();++i){
        ListNode* pNext = new ListNode(nums[i]);
        node->next = pNext;
        node = node->next;
    }
    pHead = pHead->next;
    pHead = reverseKGroup(pHead,K);
    cout<<"[";
    for(ListNode* node = pHead;node!=NULL;node = node->next){
        if(node->next!=NULL)
            cout<<node->val<<",";
        else
        {
            cout<<node->val;
        }
        
    }
    cout<<"]";
    return 0;
}