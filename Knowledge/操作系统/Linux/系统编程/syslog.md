# syslog

## 调用demo

```

#include <stdio.h>
#include <syslog.h>

int main(int argc, char** argv)
{
    openlog(argv[0], LOG_PID | LOG_CONS | LOG_NOWAIT, LOG_LOCAL0);

    for (int i = 0; i < 100; ++i)
    {
        syslog(LOG_INFO, "this is a test\n");
    }

    closelog;
    return 0;
}


```

## 配置文件位置

Ubuntu下, syslog的配置文件位置为:
`/etc/rsyslog.d/50-default.conf`

在此文件中
```
daemon.*			-/var/log/daemon.log
kern.*				-/var/log/kern.log
lpr.*				-/var/log/lpr.log
mail.*				-/var/log/mail.log
user.*				-/var/log/user.log
```
描述了各个日志存放的位置

可以追加一行
`local5.*      /root/Desktop/test.log `
则使用`openlog(argv[0], LOG_PID, LOG_LOCAL5)`
生成的日志就会存放在/root/Desktop/test.log中
