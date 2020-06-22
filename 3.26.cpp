1.给一个长度为n的数组，要求将第k位之后的值放到数组前面，比如1 2 3 4 5 6，k = 3，变换后的结果为5 6 1 2 3 4
int[] reverse(int[] array, int k){
vecor<int> newArray;
int length = array.size();
for(int i = k;i<length;++i){
newArray.push_back(array[i]);
}
for(int i = 0;i<k;++i){
newArray.push_back(array[i]);
}
return newArray;
}


2.定义：已知两个字符串s和t，现在可以对s在任意位置执行三种操作：插入一个字符；删除一个字符；替换一个字符，求将s变成t所需要的最少操作次数
int editDistance(String s , String t) {


}


3.给一个长度为n的数组a，有q组询问，q远大于n，每组询问是一个区间，现允许重排这n个数字，要求q组询问的区间和的总和最大，求这个最大值

举例：比如数组{2,0,1,0,3,4,5,6}，两组询问[2,4]和[4,6]，最优的重排方式为{0,0,2,3,6,4,5,1}，这样重排后2~4区间的和就是a[2]+a[3]+a[4]=11，4~6区间的和就是a[4]+a[5]+a[6]=15，总和为11+15=26，由于没有别的排列方式可以得到比26更大的数字，所以答案是26

double getMaxSumInRequest(int[] array, vector<vector<int>> queryList ) {
    int nums = new int[array.size()];
    for(int i =0;i<queryList.size();++i){
        vector<int> temp;
        temp = queryList.pop_back();
        for(int j=0;j<temp().size();++j)
            nums[temp.pop_back()]+=1;
        }
    sort(array,array+array.size());
    sort(nums,nums+nums.size());
    int newArray = new int[array.size()];
    for(int i=0;i<array;++i){
        newArray[i] = i;
    }
}
