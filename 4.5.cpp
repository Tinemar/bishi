#include <iostream>
#include <algorithm>
#include <vector>
#include<sstream>
using namespace std;
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


TreeNode* create(vector<int> a,int n)
 {
     TreeNode *ptree=(TreeNode*)malloc(sizeof(TreeNode )*n);
     int i;
     for(i=0;i<n;i++)
     {
         ptree[i].val=a[i];
         ptree[i].left=NULL;
         ptree[i].right=NULL;
     }
     for(i=0;i<=n/2-1;i++)
     {
         if(2*i+1<=n-1)
             ptree[i].left=&ptree[2*i+1];
         if(2*i+2<=n-1)
             ptree[i].right=&ptree[2*i+2];
     }
     return ptree;
}
void preorder(TreeNode* t)
{
    if(t==NULL) return ;
        printf("%d\n",t->val);
    preorder(t->left);
    preorder(t->right);
}
bool isValidBSTHelper(TreeNode* root, long lower, long upper){
        if(root == NULL)
            return true;
        if(root->val>=upper || root->val<=lower)
            return false;
        return isValidBSTHelper(root->left,lower,root->val)&&isValidBSTHelper(root->right,root->val,upper);
}
bool isValidBST(TreeNode* root) {
        return isValidBSTHelper(root, 0, 65536);
}
int main()
{
    string s;
    vector<int> v;
    getline(cin, s);
    istringstream is(s);
    cout<<s<<endl;
    int inter;
    char ch;
    while (is >> inter)
    {
         v.push_back(inter);
         is >> ch;
    }

    int length = v.size();
    TreeNode* root = NULL;
    root = create(v,v.size());
    cout<<isValidBST(root)<<endl;
    return 0;
}
