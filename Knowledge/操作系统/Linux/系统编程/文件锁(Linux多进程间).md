# 文件锁(Linux多进程间)

之前对于文件的操作通常在一个进程中完成，最近需要在两个进程中对同一个文件进行操作。故想到了文件锁。 
linux下可以使用flock（）函数对文件进行加锁解锁等操作。简单介绍下flock()函数：
      表头文件  #include
定义函数  int flock(int fd,int operation);
函数说明  flock()会依参数operation所指定的方式对参数fd所指的文件做各种锁定或解除锁定的动作。此函数只能锁定整个文件，无法锁定文件的某一区域。
参数  operation有下列四种情况:
LOCK_SH 建立共享锁定。多个进程可同时对同一个文件作共享锁定。
LOCK_EX 建立互斥锁定。一个文件同时只有一个互斥锁定。
LOCK_UN 解除文件锁定状态。
LOCK_NB 无法建立锁定时，此操作可不被阻断，马上返回进程。通常与LOCK_SH或LOCK_EX 做OR(|)组合。
单一文件无法同时建立共享锁定和互斥锁定，而当使用dup()或fork()时文件描述词不会继承此种锁定。
返回值  返回0表示成功，若有错误则返回-1，错误代码存于errno。
为了更好的移植性，对于文件的打开与关闭我选择了fopen和fclose的组合，但flock的第一个参数要求的是int类型的文件描述符。这里对fopen返回的FILE类型的文件指针进行转换，转换为int型的文件描述符（假设open函数返回的文件描述符为fd，而fopen返回的文件指针为*fp，则fd等价于fp->_fileno）.
 
下面为两个进程的实例：
 
```

int main(void)
{
    FILE *fp = NULL;
    int i = 20; 
    
    if ((fp = fopen("./file_lock.test", "r+b")) == NULL) //打开文件
        printf("file open error!\n");
    if (flock(fp->_fileno, LOCK_EX) != 0) //给该文件加锁
        printf("file lock by others\n");
    while(1) //进入循环,加锁时间为20秒,打印倒计时
    {   
        printf("%d\n", i--); 
        sleep(1);
        if (i == 0)
            break;
    }   
    fclose(fp); //20秒后退出,关闭文件
    flock(fp->_fileno, LOCK_UN); //文件解锁
    return 0;
 
}


int main(void)
{
    FILE *fp = NULL;
    int i = 0;
    
    if ((fp = fopen("./file_lock.test", "r+b")) == NULL) //打开文件
        printf("file open error!\n");
    flock(fp->_fileno, LOCK_EX); //文件加锁
    while(1) //进入循环
    {   
        printf("%d\n", i++); 
        sleep(1);
    }   
    fclose(fp); //关闭文件
    flock(fp->_fileno, LOCK_UN); //释放文件锁
    return 0;
 
}
```
首先运行file1.c,紧接着运行file2.c（运行file1.c后20秒内要运行file2.c否则看不到现象）
现象是:file1.c执行起来以后，开始倒计时。此时运行file2.c会阻塞在加锁处。当file1.c运行20秒后关闭文件，并释放文件锁后，file2.c会开始运行
