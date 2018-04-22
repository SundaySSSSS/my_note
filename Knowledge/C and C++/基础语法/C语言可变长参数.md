# C语言可变长参数

封装printf等带有可边长参数的函数的方法
例如:
如下是要求用户注册写日志的函数, 当需要写日志时, 进行回调

```
#include <stdarg.h>

void Utils::writeLog(const char* fmt, ...)
{
	static char log_content[512] = {0};

	if (m_log_callback == NULL)
		return;
	va_list args;
	va_start(args, fmt);
	vsnprintf(log_content, sizeof(log_content), fmt, args);
	va_end(args);
	m_log_callback(log_content);
}
```
其中`m_log_callback`是外部注册进来的回调函数, 形式为:
`void (*m_log_callback)(const char* log);`