# QT执行bat或shell命令

## 执行windows的bat命令
``` C++
QProcess p(0);
p.start("cmd");
p.waitForStarted();
p.write("dir\n");
p.closeWriteChannel();
p.waitForFinished();

```

注意: 命令中必须要有\n结尾, 否则不执行

## 执行Linux shell命令
官方文档中的例子:

``` C++
QString program = "./path/to/Qt/examples/widgets/analogclock";
QStringList arguments;
arguments << "-style" << "fusion";

QProcess *myProcess = new QProcess(parent);
myProcess->start(program, arguments);
```

## 例子 在Qt中调用windows命令删除文件夹
``` C++
QString deletePath = "C:\test";
QProcess p(NULL);
QString cmd = "rmdir /s /q " + deletePath + "\n";
p.start("cmd");
p.waitForStarted();
p.write(cmd.toLocal8Bit());
p.closeWriteChannel();
p.waitForFinished();
```