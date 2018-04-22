# queue基本使用方法
## 创建:
`queue<T> m_queue;`
## 检查当前队列大小:

`m_queue.size()`

## Push:
```
T t;
m_queue.push(t);
```
## Pop:
```
if (m_queue.size() > 0)
{
	t = m_queue.front();
	m_queue.pop();
}
```
备注: queue的pop方法不返回pop出去的元素, 所以需要先用front方法取出队首元素, 再pop
