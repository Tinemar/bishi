#include "apue.h"
int glob = 6;
char buff[];

int main(){
    int var;
    pid_t pid;
    var = 88;
    if(write(STDIO_FILENO,buf,sizeof(buf)-1))
        err_sys("writr error");
    printf("before fork\n");
    if((pid=fork())<0)
        err_sys("error");
    else if(pid==0){
        glob++;
        var++;
    }
    else{
        sleep(2);
    }
}