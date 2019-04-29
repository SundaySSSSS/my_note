# Qt 串口通信
使用qt中的串口通信的时候需要用到的两个头文件分别为：
``` C++
#include <QtSerialPort/QSerialPort>
#include <QtSerialPort/QSerialPortInfo>
```
除了加上面两个头文件之外，还需要在工程文件中加下面一行代码：
```
QT += serialport
```
我们一般都需要先定义一个全局的串口对象，记得在自己的头文件中添加上：
``` C++
QSerialPort *serial;
```

到这里我们就可以调用qt串口通信中的函数了，一般来讲qt串口通信需要经过7步:

1、设置串口名（如COM1）
``` C++
 serial = new QSerialPort;
 serial->setPortName(ui->PortBox->currentText());
 ```
这里我使用自动寻找可用串口的方法，直接自动设置了

``` C++
 foreach (const QSerialPortInfo &info,QSerialPortInfo::availablePorts())
    {
        QSerialPort serial;
        serial.setPort(info);
        if(serial.open(QIODevice::ReadWrite))
        {
            ui->PortBox->addItem(serial.portName());
            serial.close();
        }
    }
```
2、打开串口
``` C++
serial->open(QIODevice::ReadWrite);
```
3、设置波特率（如115200）

``` C++
 serial->setBaudRate(QSerialPort::Baud115200);//设置波特率为115200
```
4、设置数据位（如8）
``` C++
 serial->setDataBits(QSerialPort::Data8);//设置数据位8
```
 
5、设置校验位（如0）

``` C++
serial->setParity(QSerialPort::NoParity); //校验位设置为0
```

6、设置停止位（如1）
``` C++
 serial->setStopBits(QSerialPort::OneStop);//停止位设置为1
```
7、设置流控制
``` C++
 serial->setFlowControl(QSerialPort::NoFlowControl);//设置为无流控制
```

到这里串口通信的设置就完成了，下面我们需要实现对数据的发送和接收

1、连接数据接收槽函数，下位机中一有数据发送过来的时候就会响应这个槽函数
``` C++
QObject::connect(serial,&QSerialPort::readyRead,this,&MainWindow::ReadData);
```
在绑定的槽函数中, 调用`serial->readAll()`读取全部全部数据

2、从上位机发送数据到下位机
``` C++
serial->write(ui->textEdit_2->toPlainText().toLatin1());
```