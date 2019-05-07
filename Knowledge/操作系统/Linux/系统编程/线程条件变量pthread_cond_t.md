# 线程条件变量

## 相关函数

```
int pthread_cond_init(pthread_cond_t* cond, const pthread_condattr_t* attr);
int pthread_cond_destroy(pthread_cond_t *cond);

/*
pthread_cond_wait死等cond满足条件
pthread_cond_timedwait在tsptr时间内等待cond满足条件, 超时后返回错误ETIMEDOUT
*/
int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex);
int pthread_cond_timedwait(pthread_cond_t *cond, pthread_mutex_t* mutex, const struct timespec* tsptr);

/*
pthread_cond_signal函数至少能唤醒一个等待该条件的线程
pthread_cond_broadcast函数则会唤醒所有等待该条件的线程
*/
int pthread_cond_signal(pthread_cond_t *cond);
int pthread_cond_broadcast(pthread_cond_t *cond);
/* 上述所有函数, 返回0成功, 否则返回错误号 */
```

## pthread_cond_wait的内部操作
条件变量cond总与一个互斥量mutex相关联  
在执行pthread_cond_wait()时, 执行如下操作:  

1. 解锁互斥量mutex  
2. 阻塞调用线程, 直至另一线程对条件变量cond发出信号  
3. 重新锁定mutex  


## 实例  

```
#include <time.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

static pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

static int avail = 0;

/* 生产者线程, 每隔一秒生成一个资源 */
static void *producer(void *arg)
{
    while (1)
    {
        sleep(1);
        pthread_mutex_lock(&mtx);
        avail++;        //生产一个单位的资源
        printf("Producted\n");
        pthread_mutex_unlock(&mtx);
        pthread_cond_signal(&cond);         /* 唤醒沉睡的线程 */
    }
    return NULL;
}

int main(int argc, char *argv[])
{
    pthread_t tid;
    int s;

    pthread_create(&tid, NULL, producer, NULL);

    /* 消费者, 当存在资源时被唤醒, 进行消费 */
    while (1) 
    {
        pthread_mutex_lock(&mtx);

        while (avail == 0) 
        {   //等待被唤醒
            pthread_cond_wait(&cond, &mtx);
        }

        if (avail > 0) 
        {
            avail--;
            printf("Consumed\n");
        }

        pthread_mutex_unlock(&mtx);
    }

    exit(0);
}

```
