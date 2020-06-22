//两个栈实现队列的入队和出队操作
template <typename T>
void CQueue<T>::appendTail(const T &element)
{
    stack1.push(element);
}
template <typename T>
T CQueue<T>::deleteHead()
{
    if (stack2.size() <= 0)
    {
        while (stack1.size() > 0)
        {
            T &data = stack1.top();
            stack1.pop();
            stack2.push(data);
        }
    }
    if (stack2.size == 0)
    {
        throw new exception("queue is empty");
    }
    T head = stack2.top();
    stack2.pop();
    return head;
}
int Min(int *numbers, int length)
{
    if (numbers == nullptr || length <= 0)
    {
        throw new std::exception("error");
    }
    int index1 = 0;
    int index2 = length - 1;
    int indexMid = index1;
    while (numbers[index1] >= numbers[index2])
    {
        if (index2 - index1 == 1)
        {
            indexMid = numbers[index2];
            break;
        }
        indexMid = (index1 + index2) / 2;
        if (numbers[indexMid] >= numbers[index1])
        {
            index1 = indexMid;
        }
        if (numbers[indexMid] <= numbers[index2])
        {
            index2 = indexMid;
        }
    }
    return numbers[indexMid]
}
//剪绳子 动态规划
int maxLength(int length)
{
    int products = new int[length + 1];
    products[0] = 0;
    products[1] = 0;
    products[2] = 1;
    products[3] = 3;
    int max = 0;
    for (int i = 4; i <= length; ++i)
    {
        max = 0;
        for (int j = 1; j <= i / 2; ++j)
        {
            int product = products[i] * products[i - j];
            if (max < product)
            {
                max = product;
            }
            products[i] = max;
        }
    }
    max = products[length];
    return max;
}
//贪心 n>=5时尽量剪3的长度
int maxLength(int length)
{
    if (length < 2)
    {
        return 0;
    }
    if (length == 2)
    {
        return 2;
    }
    if (length == 3)
    {
        return 3;
    }
    int timesof3 = length / 3;
    if (length - timesof3 * 3 == 1)
    {
        timesof3 -= 1;
    }
    int timeof2 = (length - 3 * timesof3) / 2;
    return (int)(pow(3, timesof3)) * (int)(pow(2 * timeof2));
}
//18
void DeleteNode(ListNode **pListHead, ListNode *pToBeDeleted)
{
    if (!pListHead || !pToBeDeleted)
        return;
    if (pToBeDeleted->m_pNext != Null)
    {
        ListNode *pNext = pToBeDeleted->m_pNext;
        pToBeDeleted->m_nValue = pNext->m_nValue;
        pToBeDeleted->m_pNext = pNext->m_pNext;
        delete pToBeDeleted;
        pNext = nullptr;
    }
    else if (*pListHead==pToBeDeleted){
        delete pToBeDeleted;
        *pListHead = nullptr;
        pToBeDeleted = nullptr;
    }
    //删除尾节点
    else{
        ListNode* pNode = *pListHead;
        while(pNode->m_pNext!=pToBeDeleted){
            pNopde = pNode->m_pNext;
        }
        pNode->m_pNext = nullptr;
        delete pToBeDeleted;
        pToBeDeleted = nullptr;
    }
}