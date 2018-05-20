# QT自定义信号
```C++
//!!! Qt5
#include <QObject>
 
////////// newspaper.h
class Newspaper : public QObject
{
    Q_OBJECT
public:
    Newspaper(const QString & name) :
        m_name(name)
    {
    }
 
    void send()
    {
        emit newPaper(m_name);
    }
 
signals:
    void newPaper(const QString &name);
 
private:
    QString m_name;
};
 
////////// reader.h
#include <QObject>
#include <QDebug>
 
class Reader : public QObject
{
    Q_OBJECT
public:
    Reader() {}
 
    void receiveNewspaper(const QString & name)
    {
        qDebug() << "Receives Newspaper: " << name;
    }
};
 
////////// main.cpp
#include <QCoreApplication>
 
#include "newspaper.h"
#include "reader.h"
 
int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);
 
    Newspaper newspaper("Newspaper A");
    Reader reader;
    QObject::connect(&newspaper, SIGNAL(newPaper(QString),
                     &reader,    SLOT(receiveNewspaper(QString)));
    newspaper.send();
 
    return app.exec();
}
```