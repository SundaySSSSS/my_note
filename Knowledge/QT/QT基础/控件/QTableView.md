# QTableView
h文件
``` C++
#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QTableView>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = 0);
    ~Widget();

private slots:
    void on_pushButton_add_clicked();

    void on_pushButton_del_clicked();

private:
    Ui::Widget *ui;
    QTableView* m_pTableView;
};

#endif // WIDGET_H

```

cpp文件
``` C++
#include "widget.h"
#include "ui_widget.h"
#include <QStandardItemModel>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    m_pTableView = ui->tableView;
    QStandardItemModel* pModel = new QStandardItemModel();
    m_pTableView->setModel(pModel);
    QStringList headers;
    headers << "学号" << "性别" << "年龄";
    pModel->setHorizontalHeaderLabels(headers);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_pushButton_add_clicked()
{
    QStandardItemModel* pModel = (QStandardItemModel*)m_pTableView->model();
    QList<QStandardItem *> items;
    static int stuNum = 90010;
    static int age = 15;
    items.append(new QStandardItem(QString::number(stuNum)));
    items.append(new QStandardItem("男"));
    items.append(new QStandardItem(QString::number(age)));
    pModel->appendRow(items);

    stuNum++;
    age++;
}

void Widget::on_pushButton_del_clicked()
{
    QModelIndex index = m_pTableView->selectionModel()->currentIndex();
    int iSel = index.row();
    if (iSel < 0)
    {   //未选中任何行
        return;
    }
    QStandardItemModel* pModel = (QStandardItemModel*)m_pTableView->model();
    pModel->removeRow(iSel);
}

```