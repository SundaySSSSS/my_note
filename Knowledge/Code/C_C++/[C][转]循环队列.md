# [C][转]循环队列

[queue.h]
```

#ifndef __QUEUE_H_  
#define __QUEUE_H_  
typedef struct queue   
{  
    int *pBase;  
    int front;    //指向队列第一个元素  
    int rear;    //指向队列最后一个元素的下一个元素  
    int maxsize; //循环队列的最大存储空间  
}QUEUE,*PQUEUE;  
  
void CreateQueue(PQUEUE Q,int maxsize);  
void TraverseQueue(PQUEUE Q);  
bool FullQueue(PQUEUE Q);  
bool EmptyQueue(PQUEUE Q);  
bool Enqueue(PQUEUE Q, int val);  
bool Dequeue(PQUEUE Q, int *val);  

#endif  

```


[queue.c]
```
#include<stdio.h>  
#include<stdlib.h>  
#include"malloc.h"  
#include"queue.h"  
/*********************************************** 
Function: Create a empty stack; 
************************************************/  
void CreateQueue(PQUEUE Q,int maxsize)  
{  
    Q->pBase=(int *)malloc(sizeof(int)*maxsize);  
    if(NULL==Q->pBase)  
    {  
        printf("Memory allocation failure");  
        exit(-1);        //退出程序  
    }  
    Q->front=0;         //初始化参数  
    Q->rear=0;  
    Q->maxsize=maxsize;  
}  
/*********************************************** 
Function: Print the stack element; 
************************************************/  
void TraverseQueue(PQUEUE Q)  
{  
    int i=Q->front;  
    printf("队中的元素是:\n");  
    while(i%Q->maxsize!=Q->rear)  
    {  
        printf("%d ",Q->pBase[i]);  
        i++;  
    }  
    printf("\n");  
}  
bool FullQueue(PQUEUE Q)  
{  
    if(Q->front==(Q->rear+1)%Q->maxsize)    //判断循环链表是否满，留一个预留空间不用  
        return true;  
    else  
        return false;  
}  
bool EmptyQueue(PQUEUE Q)  
{  
    if(Q->front==Q->rear)    //判断是否为空  
        return true;  
    else  
        return false;  
}  
bool Enqueue(PQUEUE Q, int val)  
{  
    if(FullQueue(Q))  
        return false;  
    else  
    {  
        Q->pBase[Q->rear]=val;  
        Q->rear=(Q->rear+1)%Q->maxsize;  
        return true;  
    }  
}  
  
bool Dequeue(PQUEUE Q, int *val)  
{  
    if(EmptyQueue(Q))  
    {  
        return false;  
    }  
    else  
    {  
        *val=Q->pBase[Q->front];  
        Q->front=(Q->front+1)%Q->maxsize;  
        return true;  
    }  

}  

```
