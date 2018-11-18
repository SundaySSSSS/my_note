# QT socket
## TCP
### 基础
在pro文件中加入
`QT += network`

相关头文件:
```
#include <QTcpSocket>
#include <QTcpServer>
```

QTCPServer的相关槽函数:
```
void newConnection()
```

QTcpSocket的相关槽函数
```
void readyRead();
void connected();
void disconnected();
void error(QAbstractSocket::SocketError socketError);
```

QTcpServer相关操作
```
//监听
bool ok = server.listen(QHostAddress::AnyIPv4, 8888);

//获取连接
QTcpSocket *socket = server.nextPendingConnection();

```

socket相关操作
```
//读
QByteArray data = socket->readAll();
//写
QString msgInput = ui->textInput->toPlainText();
client->write(msgInput.toLocal8Bit());
```

### 代码示例
服务器代码
``` C++
#include "widget.h"
#include "ui_widget.h"
#include <QDebug>
#include <QHostAddress>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    connect(&server, SIGNAL(newConnection()), this, SLOT(onNewConnection()));
    bool ok = server.listen(QHostAddress::AnyIPv4, 8888);
    qDebug() << "listen 8888 " << ok;
}

Widget::~Widget()
{
    delete ui;
}

void Widget::onNewConnection()
{
    //使用这个socket和客户端进行通信
    QTcpSocket *socket = server.nextPendingConnection();
    connect(socket, SIGNAL(readyRead()), this, SLOT(onReadyRead()));
    connect(socket, SIGNAL(connected()), this, SLOT(onConnected()));
    connect(socket, SIGNAL(disconnected()), this, SLOT(onDisconnected()));
    connect(socket, SIGNAL(error(QAbstractSocket::SocketError)), this, SLOT(onError(QAbstractSocket::SocketError)));
    clients.append(socket);
}

void Widget::onReadyRead()
{
    QObject *obj = this->sender();
    QTcpSocket * socket = qobject_cast<QTcpSocket*>(obj);
    QByteArray data = socket->readAll();

    ui->textMsg->append(data);

    qDebug() << data;
}

void Widget::onConnected()  //连接成功
{
    qDebug() << "connected!";
}

void Widget::onDisconnected()   //连接断开
{
    qDebug() << "disconnected!";
    QObject *obj = this->sender();
    QTcpSocket * socket = qobject_cast<QTcpSocket*>(obj);
    clients.removeAll(socket);
    socket->deleteLater();
}

void Widget::onError(QAbstractSocket::SocketError socketError)
{
    qDebug() << "error: " << socketError;
}


void Widget::on_sendBtn_clicked()
{
    for (QList<QTcpSocket*>::iterator itr = clients.begin(); itr != clients.end(); ++itr)
    {
        QTcpSocket* client = *itr;
        QString msgInput = ui->textInput->toPlainText();
        client->write(msgInput.toLocal8Bit());
    }
}
```

client代码
``` C++
#include "widget.h"
#include "ui_widget.h"
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    connect(&socket, SIGNAL(readyRead()), this, SLOT(onReadyRead()));
    connect(&socket, SIGNAL(connected()), this, SLOT(onConnected()));
    connect(&socket, SIGNAL(disconnected()), this, SLOT(onDisconnected()));
    connect(&socket, SIGNAL(error(QAbstractSocket::SocketError)), this, SLOT(onError(QAbstractSocket::SocketError)));
    socket.connectToHost("127.0.0.1", 8888);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::onReadyRead()
{
    QObject *obj = this->sender();
    QTcpSocket * socket = qobject_cast<QTcpSocket*>(obj);
    QByteArray data = socket->readAll();
    qDebug() << data;
    ui->textMsg->append(data);
}

void Widget::onConnected()  //连接成功
{
    qDebug() << "connected!";
}

void Widget::onDisconnected()   //连接断开
{
    qDebug() << "disconnected!";
    socket.deleteLater();
}

void Widget::onError(QAbstractSocket::SocketError socketError)
{
    qDebug() << "error: " << socketError;
}

void Widget::on_sendBtn_clicked()
{
    QString msgInput = ui->textInput->toPlainText();
    socket.write(msgInput.toLocal8Bit());
}
```

