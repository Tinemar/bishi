void remove(char* s,char x){
    int numofspace = 0;
    int length = 0;
    int i=0;
    while(s[i]!='\0'){
        length++;
        if(s[i] == x){
            numofspace++;
        }
        i++;
    }
    int newlength = length-numofspace;
    if(newlength==length){
        return;
    }
    int olds = 0;
    int news = 0;
    while(olds<length){
        if(s[olds]==x){
            olds++;
            s[news] = s[olds];
        }
        else{
            s[news] == s[olds];
        }
        olds++;
        news++;
    }
    return;
}