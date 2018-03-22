# glog基本用法

## glog安装
```
./configure
make
```

交叉编译:
8127
`./configure --host=arm-arago-linux-gnueabi`
6467_2009q1 <-编译不过...
`./configure --host=arm-none-linux-gnueabi`

前提是交叉编译器（8127， 8168）的所在路径必须已经在PATH环境变量中

再make即可

生成的动态库和静态库在`.libs`目录里(默认隐藏)
`libglog.a` `libglog.so`

## 最简单Demo
```
#include <glog/logging.h>
int main(int argc,char* argv[])
{
    LOG(INFO) << "Hello,GLOG!";
}
```

## glog工具类
```C++
#include <pthread.h>
#include <stdio.h>
#include <signal.h>
#include <string>
#include "glog/logging.h"

using namespace std;

class GLogHelper
{
public:
    //GLOG配置：
    GLogHelper(const char* program, const char* path);
    //GLOG内存清理：
    ~GLogHelper();
};


//GLOG配置：
GLogHelper::GLogHelper(const char* program, const char* path)
{
	string program_str;
	string path_str;
	
	if (program == NULL)
		program_str = "unknown_process";
	else
		program_str = program;
	if (path == NULL)
		path_str = "./";
	else
		path_str = path;

    //system(MKDIR);
    google::InitGoogleLogging(program_str.c_str());

    google::SetStderrLogging(google::INFO); //设置级别高于 google::INFO 的日志同时输出到屏幕
    //google::SetLogDestination(google::ERROR,"log/error_");    //设置 google::ERROR 级别的日志存储路径和文件名前缀
    google::SetLogDestination(google::INFO, path_str.c_str()); //设置 google::INFO 级别的日志存储路径和文件名前缀
    google::SetLogDestination(google::WARNING, path_str.c_str());   //设置 google::WARNING 级别的日志存储路径和文件名前缀
    google::SetLogDestination(google::ERROR, path_str.c_str());   //设置 google::ERROR 级别的日志存储路径和文件名前缀
    //FLAGS_logbufsecs =0;        //缓冲日志输出，默认为30秒，此处改为立即输出
    FLAGS_max_log_size =50;  //最大日志大小为 50MB
    FLAGS_stop_logging_if_full_disk = true;     //当磁盘被写满时，停止日志输出
    google::InstallFailureSignalHandler();      //捕捉 core dumped
    //google::InstallFailureWriter(&SignalHandle);    //默认捕捉 SIGSEGV 信号信息输出会输出到 stderr，可以通过下面的方法自定义输出>方式：
}

//GLOG内存清理：
GLogHelper::~GLogHelper()
{
    google::ShutdownGoogleLogging();
}

int main(int argc,char* argv[])
{
	GLogHelper gLH(argv[0], "./log/");
	while(1)
	{
		sleep(1);
    	LOG(INFO) << "Hello,GLOG!";
    }
    return 1;
}

```

## 让glog每天生成一个新文件

glog默认是根据进程ID是否改变和文件大小是否超过预定值来确定是否需要新建日志文件的，此处可以参考glog源码 logging.cc 文件中的 void LogFileObject::Write 函数中
```
if (static_cast<int>(file_length_ >> 20) >= MaxLogSize() ||
    PidHasChanged()) {
```

我们只需要在此处加一个日期判断就可以了，PidHasChanged() 定义于 utilities.cc 文件中，可以加一个类似的 DayHasChanged() 函数（注意 utilities.h 文件中加上函数声明）：

```
static int32 g_main_day = 0;bool DayHasChanged()
{
    time_t raw_time;
    struct tm* tm_info;

    time(&raw_time);
    tm_info = localtime(&raw_time);

    if (tm_info->tm_mday != g_main_day)
    {
        g_main_day = tm_info->tm_mday;
        return true;
    }

    return false;
}
```

再修改 void LogFileObject::Write 函数中的判断条件即可：
```
if (static_cast<int>(file_length_ >> 20) >= MaxLogSize() ||
 PidHasChanged() || DayHasChanged()) {
```


