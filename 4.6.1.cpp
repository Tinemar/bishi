#include <stdio.h>
#include <iostream>
#include <istream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int numsOf(vector<int> card)
{
    int count = 0;
    int begin = 1, end = 1;
    for (int k = 1; k <= 13; ++k)
    {
        if (card[k])
        {
            end = k;
        }
        else
        {
            int len = end - begin + 1;
            if (len >= 5)
            {
                for (int b = begin; b <= end - 4; ++b)
                {
                    for (int e = end; e >= b + 4; --e)
                    {
                        int tmp = 1;
                        for (int g = b; g <= e; ++g)
                        {
                            tmp *= card[g];
                        }
                        count += tmp;
                    }
                }
            }
            begin = k;
        }
    }
    return count;
}
int main()
{
    int T;
    cin >> T;
    vector<vector<int>> cards;
    for (int i = 0; i < T; ++i)
    {
        int N;
        cin >> N;
        vector<int> card(14, 0);
        for (int j = 0; j < N; ++j)
        {
            char c;
            cin >> c;
            switch (c)
            {
            case 'A':
                card[1] += 1;
                break;
            case 'J':
                card[11] += 1;
                break;
            case 'Q':
                card[12] += 1;
                break;
            case 'K':
                card[13] += 1;
            default:
                card[c - '0'] += 1;
                break;
            }
        }
        cards.push_back(card);
    }
    for (int i = 0; i < T; ++i)
    {
        int result = numsOf(cards[i]);
        cout << result;
        if(i!=T-1)
            cout<<endl;
    }
    return 0;
}
