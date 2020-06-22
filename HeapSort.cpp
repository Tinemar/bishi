//https://blog.csdn.net/morewindows/article/details/6709644
//新加入节点i，父节点是(i-1)/2
void MinHeapFixup(int a[],int i){
    int temp = a[i];
    int j = (i-1)/2;
    while(j>=0 && i!=0){
        if(a[j]<a[i])
            break;
        else
        {
            a[i] = a[j];
            i=j;
            j=(i-1)/2;
        }
    }
    a[j] = temp;
}
//插入元素
void MinHeapAddNumber(int a[],int n,int nNum){
    a[n] = nNum;
    MinHeapFixup(a,n);
}
//删除节点时的下滤，n为节点总数，从第i个节点开始调整
void MinHeapFixdown(int a[],int i,int n){
    int temp = a[i];
    int j = 2*i + 1;
    while(j<n){
        //左右节点最小的
        if(j+1<n && a[j+1]<a[j])
            j++;
        //
        if(temp<a[j])
            break;
        else{
            a[i] = a[j];
            i = j;
            j = 2*i + 1;
        }
    }
    a[i] = temp;
}
//删除堆顶元素
void MinHeapDeleteNumber(int a[],int n){
    swap(a[0],a[n-1]);
    MinHeapFixdown(a,0,n-1);
}
//构建最小堆
void MinHeapCreate(int a[],int n){
    //n/2是叶子节点外的最后一个节点
    for(int i=n/2;i>=0;--i)
        MinHeapFixdown(a,i,n);
}
// 堆排序
// 每次取出堆顶元素值，交换至数组尾部，再执行删除堆顶元素操作，
// 使堆顶元素依然是最小元素，同时尾部数组变为有序，得到递减数组
// 每次操作的堆长度依次-1
void MinHeapSort(int a[],int n){
    for(int i=n-1;i>0;--i){
        swap(a[0],a[i]);
        MinHeapFixdown(a,0,i);
    }
}