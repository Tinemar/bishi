#include <iostream>
#include<algorithm>
using namespace std;

void swap2(float &p1, float &p2) //此处函数的形参p1, p2都是引用
{
        int p;
        p=p1;
        p1=p2;
        p2=p; 
}
int main()
{
    int m, n;
    cin >> m >> n;
    float x = float(m);
    float y = float(n);
    if (x == y)
    {
        cout << m+1;
    }
    else
    {
        x += 1;
        y += 1;
        float k = y / x;
        int count = 0;
        if (k >1)
        {
            k = x / y;
            swap2(x, y);
            cout<<x<<y<<endl;
        }
        for (float x_i = 1; x_i < x; ++x_i)
        {
            if (x_i * k < x_i)
            {
                count += 2;
            }
            else
            {
                count += 1;
            }
        }
        cout << count;
    }

    return 0;
}