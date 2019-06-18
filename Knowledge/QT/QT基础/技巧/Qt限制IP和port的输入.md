# Qt限制IP和port的输入
``` C++
#include "widget.h"
#include "ui_widget.h"
#include <QRegExpValidator>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    QLineEdit *pIPLineEdit = ui->lineEdit_IP;
    //QRegExp rx("((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))");
    QRegExp rx("((?:(?:25[0-5]|2[0-4]\\d|((1\\d{2})|([1-9]?\\d)))\\.){3}(?:25[0-5]|2[0-4]\\d|((1\\d{2})|([1-9]?\\d))))");
    pIPLineEdit->setValidator(new QRegExpValidator(rx, this));

    QLineEdit *pPortLineEdit = ui->lineEdit_Port;
    QValidator *validator = new QIntValidator(1024, 65535, this);
    pPortLineEdit->setValidator(validator);
}

Widget::~Widget()
{
    delete ui;
}

```