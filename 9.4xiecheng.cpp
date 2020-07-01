#include <iostream>
#include <vector>
#include <numeric>
#include <limits>
#include<algorithm>
using namespace std;

class ListNode {
public:
    int val;
    ListNode* next;
    ListNode(int val){
        this->val=val;
        this->next=NULL;
    };
};

/*请完成下面这个函数，实现题目要求的功能
******************************开始写代码******************************/
ListNode* partition(ListNode* head,int m) {
    ListNode* node = head;
    ListNode* pre = NULL;
    pre->next = node;
    ListNode* newhead = head;
    while(node!=NULL){
        if(node->val<=m){
            ListNode* tmp = node;
            pre->next = tmp->next;
            node->next = newhead;
            newhead = node;
            pre = pre->next;
            node = tmp->next;
        }
        else{
            pre = pre->next;
            pre->next = node->next;
            node = node->next;
        }
    }
    return newhead;
}
/******************************结束写代码******************************/


int main() {
    ListNode* head=NULL;
    ListNode* node=NULL;
    int m;
    cin>>m;
    int v;
    while(cin>>v){
        if(head==NULL){
            node=new ListNode(v);
            head=node;
        }else{
            node->next=new ListNode(v);
            node=node->next;
        }
    }
    head = partition(head,m);
    if(head!=NULL){
        cout<<head->val;
        node=head->next;
        delete head;
        head=node;
        while(head!=NULL){
            cout<<","<<head->val;
            node=head->next;
            delete head;
            head=node;
        }
    }
    cout<<endl;
    return 0;
}


string resolve(string expr) {
    vector<int> k;
    vector<string> result;
    vector<vector<int>> rev;
    string result;
    for(int i=0;i<expr.size();++i){
        if(expr[i] == '('){
            k.push_back(i);
        }
        if(expr[i] == ')'){
            rev.push_back(k.back(),i);
            k.pop_back();
        }
    }
    for(it = rev.begin();it!=vec.end();it++){
        int start = *it[0];
        int end = *it[1];
        for(int i=start;i<=end;++i){
            string s;
            if(expr[i]!='(' or expr[i]!=')'){
                s += expr[i];
            }
            s = 
        }
    }
}