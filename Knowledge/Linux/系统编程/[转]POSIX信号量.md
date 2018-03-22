# [转]POSIX信号量

```
函数介绍
#include<semaphore.h>
信号量的数据类型为结构sem_t，它本质上是一个长整型的数。
函数sem_init()用来初始化一个信号量。它的原型为：int sem_init __P ((sem_t *__sem, int __pshared, unsigned int __value));sem为指向信号量结构的一个指针；pshared不为0时此信号量在进程间共享，否则只能为当前进程的所有线程共享；value给出了信号量的初始值。信号量用sem_init函数创建的，下面是它的说明：
int sem_init (sem_t *sem, int pshared, unsigned int value); 这个函数的作用是对由sem指定的信号量进行初始化，设置好它的共享选项，并指定一个整数类型的初始值。pshared参数控制着信号量的类型。如果 pshared的值是0，就表示它是当前里程的局部信号量；否则，其它进程就能够共享这个信号量。我们现在只对不让进程共享的信号量感兴趣。　（这个参数 受版本影响），pshared传递一个非零将会使函数调用失败，属于无名信号量。
sem_open功能：创建并初始化有名信号灯，参数：name   信号灯的外部名字(不能为空，为空会出现段错误)  oflag   选择创建或打开一个现有的信号灯  mode 权限位  value 信号灯初始值  返回值：成功时返回指向信号灯的指针，出错时为SEM_FAILED，oflag参数能是0（打开一个已创建的）、O_CREAT（创建一个信号灯）或O_CREAT|O_EXCL（如果没有指定的信号灯就创建），如果指定了O_CREAT，那么第三个和第四个参数是需要的；其中mode参数指定权限位，value参数指定信号灯的初始值，通常用来指定共享资源的书面。该初始不能超过 SEM_VALUE_MAX，这个常值必须低于为32767。二值信号灯的初始值通常为1，计数信号灯的初始值则往往大于1。
       如果指定了O_CREAT（而没有指定O_EXCL），那么只有所需的信号灯尚未存在时才初始化他。所需信号灯已存在条件下指定O_CREAT不是个错误。该标志的意思仅仅是“如果所需信号灯尚未存在，那就创建并初始化他”。不过所需信号灯等已存在条件下指定O_CREAT|O_EXCL却是个错误。sem_open返回指向sem_t信号灯的指针，该结构里记录着当前共享资源的数目。
sem_close 关闭有名信号灯。
若成功则返回0，否则返回-1。一个进程终止时，内核还对其上仍然打开着的所有有名信号灯自动执行这样的信号灯关闭操作。不论该进程是自愿终止的还是非自愿终止的，这种自动关闭都会发生。但应注意的是关闭一个信号灯并没有将他从系统中删除。这就是说，Posix有名信号灯至少是随内核持续的：即使当前没有进程打开着某个信号灯，他的值仍然保持。多进程打开时候，一边sem_close后，仍可以打开已经打开的信号量。
sem_unlink 从系统中删除信号灯 定义：int sem_unlink(const char *name);若成功则返回0，否则返回-1。有名信号灯使用sem_unlink从系统中删除。每个信号灯有一个引用计数器记录当前的打开次数，sem_unlink必须等待这个数为0时才能把name所指的信号灯从文件系统中删除。也就是要等待最后一个sem_close发生。
sem_getvalue 测试信号灯
函数sem_post( sem_t *sem )用来增加信号量的值。当有线程阻塞在这个信号量上时，调用这个函数会使其中的一个线程不在阻塞，选择机制同样是由线程的调度策略决定的。int sem_post(sem_t *sem);sem_post() 成功时返回 0；错误时，信号量的值没有更改，-1 被返回，并设置errno 来指明错误。错误   EINVAL sem 不是一个有效的信号量。 EOVERFLOW 信号量允许的最大值将要被超过。
函数sem_wait( sem_t *sem )被用来阻塞当前线程直到信号量sem的值大于0，解除阻塞后将sem的值减一，表明公共资源经使用后减少。
这两个函数控制着信号量的值，它们的定义如下所示：
#include <semaphore.h> int sem_wait(sem_t * sem);int sem_post(sem_t * sem);
        这两个函数都要用一个由sem_init调用初始化的信号量对象的指针做参数。
        sem_post函数的作用是给信号量的值加上一个“1”，它是一个“原子操作”－－－即同时对同一个信号量做加“1”操作的两个线程是不会冲突的；而同 时对同一个文件进行读、加和写操作的两个程序就有可能会引起冲突。信号量的值永远会正确地加一个“2”－－因为有两个线程试图改变它。
        sem_wait函数也是一个原子操作，它的作用是从信号量的值减去一个“1”，但它永远会先等待该信号量为一个非零值才开始做减法。也就是说，如果你对 一个值为2的信号量调用sem_wait(),线程将会继续执行，介信号量的值将减到1。如果对一个值为0的信号量调用sem_wait()，这个函数就 会地等待直到有其它线程增加了这个值使它不再是0为止。如果有两个线程都在sem_wait()中等待同一个信号量变成非零值，那么当它被第三个线程增加 一个“1”时，等待线程中只有一个能够对信号量做减法并继续执行，另一个还将处于等待状态。信号量这种“只用一个函数就能原子化地测试和设置”的能力下正是它的价值所在。 还有另外一个信号量函数sem_trywait，它是sem_wait的非阻塞搭档。
函数sem_trywait ( sem_t *sem )是函数sem_wait（）的非阻塞版本，它直接将信号量sem的值减一。在成功完成之后会返回零。其他任何返回值都表示出现了错误。
函数sem_destroy(sem_t *sem)用来释放信号量sem，属于无名信号量。
   最后一个信号量函数是sem_destroy。这个函数的作用是在我们用完信号量对它进行清理。下面的定义：#include<semaphore.h>int sem_destroy (sem_t *sem);
这个函数也使用一个信号量指针做参数，归还自己战胜的一切资源。在清理信号量的时候如果还有线程在等待它，用户就会收到一个错误。与其它的函数一样，这些函数在成功时都返回“0”。
 无名信号量的例子：
[cpp] view plain copy
1. #include <stdio.h>  
2. #include <unistd.h>  
3. #include <stdlib.h>  
4. #include <string.h>  
5. #include <pthread.h>  
6. #include <semaphore.h>  
7.   
8. sem_t bin_sem;  
9. void *thread_function1(void *arg)  
10. {  
11.  printf("thread_function1--------------sem_wait\n");  
12.  sem_wait(&bin_sem);  
13.  printf("sem_wait\n");  
14.  while (1)  
15.  {  
16.   printf("th1 running!\n");  
17.   sleep(1);  
18.  }  
19. }  
20.   
21. void *thread_function2(void *arg)  
22. {  
23.  printf("thread_function2--------------sem_post\n");  
24.  sem_post(&bin_sem);  
25.  printf("sem_post\n");  
26.  while (1)  
27.  {  
28.   printf("th2 running!\n");  
29.   sleep(1);  
30.  }  
31. }  
32. int main()  
33. {  
34.  int res;  
35.  pthread_t a_thread;  
36.  void *thread_result;  
37.    
38.  res = sem_init(&bin_sem, 0, 0);  
39.  if (res != 0)  
40.  {  
41.   perror("Semaphore initialization failed");  
42.  }  
43.   printf("sem_init\n");  
44.  res = pthread_create(&a_thread, NULL, thread_function1, NULL);  
45.  if (res != 0)  
46.  {  
47.   perror("Thread creation failure");  
48.  }  
49.  printf("thread_function1\n");  
50.  sleep(5);  
51.  printf("sleep\n");  
52.  res = pthread_create(&a_thread, NULL, thread_function2, NULL);  
53.  if (res != 0)  
54.  {  
55.   perror("Thread creation failure");  
56.  }  
57.  while (1)  
58.  {  
59.    printf("running !\n");  
60.    sleep(5);  
61.  }  
62. }  
运行结果：
sem_init
thread_function1
thread_function1--------------sem_wait
sleep
thread_function2--------------sem_post
sem_wait
sem_post
有名信号量在无相关进程间的同步
       有名信号量的特点是把信号量的值保存在文件中。这决定了它的用途非常广：既可以用于线程，也可以用于相关进程间，甚至是不相关进程。由于有名信号量的值是保存在文件中的，所以对于相关进程来说，子进程是继承了父进程的文件描述符，那么子进程所继承的文件描述符所指向的文件是和父进程一样的，当然文件里面保存的有名信号量值就共享了。
       有名信号量是位于共享内存区的，那么它要保护的资源也必须是位于共享内存区，只有这样才能被无相关的进程所共享。在下面这个例子中，服务进程和客户进程都使用shmget和shmat来获取得一块共享内存资源。然后利用有名信号量来对这块共享内存资源进行互斥保护。
[cpp] view plain copy
1. File1: server.c   
2. #include <sys/types.h>  
3. #include <sys/ipc.h>  
4. #include <sys/shm.h>  
5. #include <stdio.h>  
6. #include <semaphore.h>  
7. #include <sys/types.h>  
8. #include <sys/stat.h>  
9. #include <fcntl.h>  
10.   
11. #define SHMSZ 27  
12. char SEM_NAME[]= "vik";  
13.   
14. int main()  
15. {  
16.     char ch;  
17.     int shmid;  
18.     key_t key;  
19.     char *shm,*s;  
20.     sem_t *mutex;  
21.   
22.     //name the shared memory segment  
23.     key = 1000;  
24.   
25.     //create & initialize semaphore  
26.     mutex = sem_open(SEM_NAME,O_CREAT,0644,1);  
27.     if(mutex == SEM_FAILED)  
28.     {  
29.       perror("unable to create semaphore");  
30.       sem_unlink(SEM_NAME);  
31.       exit(-1);  
32.     }  
33.   
34.     //create the shared memory segment with this key  
35.     shmid = shmget(key,SHMSZ,IPC_CREAT|0666);  
36.     if(shmid<0)  
37. {  
38.         perror("failure in shmget");  
39.         exit(-1);  
40. }  
41.   
42.     //attach this segment to virtual memory  
43.     shm = shmat(shmid,NULL,0);  
44.   
45.     //start writing into memory  
46.     s = shm;  
47.     for(ch='A';ch<='Z';ch++)  
48.     {  
49.         sem_wait(mutex);  
50.         *s++ = ch;  
51.         sem_post(mutex);  
52.      }  
53.   
54.     //the below loop could be replaced by binary semaphore  
55.     while(*shm != '*')  
56.     {  
57.         sleep(1);  
58. }  
59.     sem_close(mutex);  
60.     sem_unlink(SEM_NAME);  
61.     shmctl(shmid, IPC_RMID, 0);  
62.     exit(0);  
63. }  
64.   
65. File 2: client.c  
66. #include <sys/types.h>  
67. #include <sys/ipc.h>  
68. #include <sys/shm.h>  
69. #include <stdio.h>  
70. #include <semaphore.h>  
71. #include <sys/types.h>  
72. #include <sys/stat.h>  
73. #include <fcntl.h>  
74.   
75. #define SHMSZ 27  
76. char SEM_NAME[]= "vik";  
77.   
78. int main()  
79. {  
80.     char ch;  
81.     int shmid;  
82.     key_t key;  
83.     char *shm,*s;  
84.     sem_t *mutex;  
85.   
86.     //name the shared memory segment  
87.     key = 1000;  
88.   
89.     //create & initialize existing semaphore  
90.     mutex = sem_open(SEM_NAME,0,0644,0);  
91.     if(mutex == SEM_FAILED)  
92.     {  
93.         perror("reader:unable to execute semaphore");  
94.         sem_close(mutex);  
95.         exit(-1);  
96.     }  
97.   
98.     //create the shared memory segment with this key  
99.     shmid = shmget(key,SHMSZ,0666);  
100.     if(shmid<0)  
101.     {  
102.         perror("reader:failure in shmget");  
103.         exit(-1);  
104.     }  
105.   
106.     //attach this segment to virtual memory  
107.     shm = shmat(shmid,NULL,0);  
108.   
109.     //start reading  
110.     s = shm;  
111.     for(s=shm;*s!=NULL;s++)  
112.     {  
113.         sem_wait(mutex);  
114.         putchar(*s);  
115.       sem_post(mutex);  
116.     }  
117.   
118.   //once done signal exiting of reader:This can be replaced by another semaphore  
119.     *shm = '*';  
120.     sem_close(mutex);  
121.     shmctl(shmid, IPC_RMID, 0);  
122.     exit(0);  
123. } 

```
