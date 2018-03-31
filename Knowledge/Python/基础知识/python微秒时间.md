# python微秒时间
``` python
import datetime
begin = datetime.datetime.now()
end = datetime.datetime.now()
k = end - begin
print(k)
0:00:06.360995
k.total_seconds()
6.360995
```