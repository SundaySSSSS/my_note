# 线程启动demo

```
static pthread_t m_handle;	//线程句柄

void* ProcessThread(void* arg)
{
    //do something
    return (void*) 0;
}

if((pthread_create(&m_handle, NULL, ProcessThread, NULL)) != 0)
{	//创建线程失败
    dbout("create thread error\n");
}
else
{
		pthread_detach(m_handle);
}

```
