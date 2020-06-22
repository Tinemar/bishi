#include <stdio.h>
#include <iostream>
#include <istream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int numsOf(int num)
{
    string num1 = to_string(num);
    vector<int> num2;
    int length = ((num1.size() / 3) + 1) * 3;
    int temp = 0;
    int count = 0;
    //diyibu
    for (int i = 0; i < length; ++i)
    {
        if (count < 2)
            temp += (num1[i] - '0') * 10;
        else
        {
            num2.push_back(temp);
            count = 0;
        }
    }
}
int main()
{
    int T;
    cin >> T;
    vector<int> nums;
    for (int i = 0; i < T; ++i)
    {
        int N;
        cin >> N;
        nums.push_back(N);
    }
    for (int i = 0; i < T; ++i)
    {
        int result = numsOf(nums[i]);
        cout << result;
        if (i != T - 1)
            cout << endl;
    }
    return 0;
}
int main()
{
    int T;
    cin >> T;
    for (size_t i = 0; i < T; ++i)
    {
        string ret;
        string num;
        cin >> num;
        switch (num.size() % 3)
        {
        case 1:
            num = "00" + num;
            break;
        case 2:
            num = "0" + num;
            break;
        default:
            break;
        }
        for (int i = 0; i < num.size(); i += 3)
        {
            int tmp = (num[i] - '0') * 100 + (num[i + 1] - '0') * 10 + (num[i + 2] - '0');
            int h = tmp >> 5;
            int l = tmp & 31;
            ret += (h >= 10) ? h - 10 + 'A' : h + '0';
            ret += (l >= 10) ? l - 10 + 'A' : l + '0';
        }
        if (ret[0] == '0')
            ret.erase(0, 1);
        cout << ret << endl;
    }
}