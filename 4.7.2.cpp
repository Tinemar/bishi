#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int middle(vector<int> num)
{
    return num[num.size() / 2];
}
int main()
{
    int N;
    cin >> N;
    vector<int> num;
    vector<int> result;
    for(int i=0;i<N+1;++i)
    {
        string cmd;
        getline(cin, cmd);
        if (cmd.size() > 4 && cmd!="print")
        {
            int add_num = stoi(cmd.substr(4));
            num.push_back(add_num);
        }
        else if (cmd=="print")
        {
            sort(num.begin(), num.end());
            int m = middle(num);
            result.push_back(m);
            num.erase(num.begin() + num.size() / 2);
        }
    }
    for(int i=0;i<result.size();++i){
        cout<<result[i]<<endl;
    }
    return 0;
}