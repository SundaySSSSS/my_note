# 查找某进程(LinuxC)

## 一、前言：
要在程序中启动某一程序，如果程序已经存在了，就不再启动。查找了N篇文档，有所收获，总结一下。

## 二、实现
大体分两种：
### 1、通过ps命令 [在8127上实验, 可行]
exec或popen执行ps的命令行，然后运用某几个字符串匹配函数。
```
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>
int main()
{
    FILE *pstr; char cmd[128],buff[512],*p;
    pid_t pID;
    int pidnum;
    char *name= "ping ";//要查找的进程名
    int ret=3;
    memset(cmd,0,sizeof(cmd));

    sprintf(cmd, "ps -ef|grep %s ",name);
    pstr=popen(cmd, "r");//    

    if(pstr==NULL)
    { return 1; }
    memset(buff,0,sizeof(buff));
    fgets(buff,512,pstr);
    p=strtok(buff, " ");
    p=strtok(NULL, " "); //这句是否去掉，取决于当前系统中ps后，进程ID号是否是第一个字段 pclose(pstr);
    if(p==NULL)
    { return 1; }
    if(strlen(p)==0)
    { return 1; }
    if((pidnum=atoi(p))==0)
    { return 1; }
    printf("pidnum: %d\n",pidnum);
    pID=(pid_t)pidnum;
    ret=kill(pID,0);//这里不是要杀死进程，而是验证一下进程是否真的存在，返回0表示真的存在
    printf("ret= %d \n",ret);
    if(0==ret)
        printf("process: %s exist!\n",name);
    else printf("process: %s not exist!\n",name);

    return 0;
}
```
问题：这里是通过那个命令返回的信息是不是空来判断有没有这个进程的。还有一些实现是通过strcmp或者strstr来实现的。但是有个明显的问题就是，如果没有ping进程，而有个ping1之类的名字中带ping的进程，grep就废了。（貌似可以通过正则表达式实现，没实验过。）
### 2、读取/proc文件
找到个代码如下：

读取/proc文件查找进程
通过比较全路径，能一定程度上避免第1种方法的问题。
以下是整理后的C语言实现：

```
#include <unistd.h>
#include <dirent.h>
#include <sys/types.h> // for opendir(), readdir(), closedir()
#include <sys/stat.h> // for stat()
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

#define PROC_DIRECTORY "/proc/"
#define CASE_SENSITIVE    1
#define CASE_INSENSITIVE  0
#define EXACT_MATCH       1
#define INEXACT_MATCH     0

//是不是数字
int IsNumeric(const char* ccharptr_CharacterList)
{
    for ( ; *ccharptr_CharacterList; ccharptr_CharacterList++)
        if (*ccharptr_CharacterList < '0' || *ccharptr_CharacterList > '9')
            return 0; // false
    return 1; // true
}

//intCaseSensitive=0大小写不敏感
int strcmp_Wrapper(const char *s1, const char *s2, int intCaseSensitive)
{
    if (intCaseSensitive)
        return !strcmp(s1, s2);
    else
        return !strcasecmp(s1, s2);
}

//intCaseSensitive=0大小写不敏感
int strstr_Wrapper(const char* haystack, const char* needle, int intCaseSensitive)
{
    if (intCaseSensitive)
        return (int) strstr(haystack, needle);
    else
        return (int) strcasestr(haystack, needle);
}

pid_t GetPIDbyName_implements(const char* cchrptr_ProcessName, int intCaseSensitiveness, int intExactMatch)
{
    char chrarry_CommandLinePath[100]  ;
    char chrarry_NameOfProcess[300]  ;
    char* chrptr_StringToCompare = NULL ;
    pid_t pid_ProcessIdentifier = (pid_t) -1 ;
    struct dirent* de_DirEntity = NULL ;
    DIR* dir_proc = NULL ;

    int (*CompareFunction) (const char*, const char*, int) ;

    if (intExactMatch)
        CompareFunction = &strcmp_Wrapper;
    else
        CompareFunction = &strstr_Wrapper;


    dir_proc = opendir(PROC_DIRECTORY) ;
    if (dir_proc == NULL)
    {
        perror("Couldn't open the " PROC_DIRECTORY " directory") ;
        return (pid_t) -2 ;
    }

    // Loop while not NULL
    while ( (de_DirEntity = readdir(dir_proc)) )
    {
        if (de_DirEntity->d_type == DT_DIR)
        {
            if (IsNumeric(de_DirEntity->d_name))
            {
                strcpy(chrarry_CommandLinePath, PROC_DIRECTORY) ;
                strcat(chrarry_CommandLinePath, de_DirEntity->d_name) ;
                strcat(chrarry_CommandLinePath, "/cmdline") ;
                FILE* fd_CmdLineFile = fopen (chrarry_CommandLinePath, "rt") ;  //open the file for reading text
                if (fd_CmdLineFile)
                {
                    fscanf(fd_CmdLineFile, "%s", chrarry_NameOfProcess) ; //read from /proc/<NR>/cmdline
                    fclose(fd_CmdLineFile);  //close the file prior to exiting the routine

                    if (strrchr(chrarry_NameOfProcess, '/'))
                        chrptr_StringToCompare = strrchr(chrarry_NameOfProcess, '/') +1 ;
                    else
                        chrptr_StringToCompare = chrarry_NameOfProcess ;

                    //printf("Process name: %s\n", chrarry_NameOfProcess);
                    //这个是全路径，比如/bin/ls
                    //printf("Pure Process name: %s\n", chrptr_StringToCompare );
                    //这个是纯进程名，比如ls

                    //这里可以比较全路径名，设置为chrarry_NameOfProcess即可
                    if ( CompareFunction(chrptr_StringToCompare, cchrptr_ProcessName, intCaseSensitiveness) )
                    {
                        pid_ProcessIdentifier = (pid_t) atoi(de_DirEntity->d_name) ;
                        closedir(dir_proc) ;
                        return pid_ProcessIdentifier ;
                    }
                }
            }
        }
    }
    closedir(dir_proc) ;
    return pid_ProcessIdentifier ;
}

    //简单实现
    pid_t GetPIDbyName_Wrapper(const char* cchrptr_ProcessName)
    {
            return GetPIDbyName_implements(cchrptr_ProcessName, 0,0);//大小写不敏感
    }

int main()
{
    pid_t pid = GetPIDbyName_Wrapper("bash") ; // If -1 = not found, if -2 = proc fs access error
    printf("PID %d\n", pid);
    return EXIT_SUCCESS ;
}

```
