#include<cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
using namespace std;
bool isThreshold(int threshold, int row, int col)
{
    int sum = 0;
    while (row > 0)
    {
        sum += row % 10;
        row /= 10;
    }
    while (col > 0)
    {
        sum += col % 10;
        col /= 10;
    }
    if (sum <= threshold)
        return true;
    return false;
}
bool check(int threshold, int rows, int cols, int row, int col, bool *visited)
{
    if (visited[cols * row + col] == 0 && row >= 0 && row < rows && col >= 0 && col < cols && isThreshold(threshold, row, col))
        return true;
    return false;
}
int Count(int threshold, int rows, int cols, int row, int col, bool *visited)
{
    int count = 0;
    if (check(threshold, rows, cols, row, col, visited))
    {
        visited[row * cols + col] = 1;
        count = 1 + Count(threshold, rows, cols, row + 1, col, visited) + Count(threshold, rows, cols, row, col + 1, visited) + Count(threshold, rows, cols, row - 1, col, visited) + Count(threshold, rows, cols, row, col - 1, visited);
    }
    return count;
}
int movingCount(int threshold, int rows, int cols)
{
    if (rows < 1 || cols < 1 || threshold < 0)
        return 0;
    bool *visited = new bool[rows * cols];
    memset(visited, 0, rows * cols);
    int count = Count(threshold, rows, cols, 0, 0, visited);
    return count;
}

int main()
{
    int threshold, rows, cols;
    cin >> rows >> cols >> threshold;
    int result = movingCount(threshold, rows, cols);
    cout << result << endl;
    return 0;
}