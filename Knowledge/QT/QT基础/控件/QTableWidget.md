# QTableWidget

## 在表格中加入控件

``` C++
QStringList headerList;
headerList << "姓名" << "性别";

m_pTable = ui->tableWidget;

m_pTable->setColumnCount(2); //必须在设定标题前设定好列数
m_pTable->setRowCount(1);
m_pTable->setHorizontalHeaderLabels(headerList);
m_pTable->verticalHeader()->hide();  //隐藏列头

QTableWidgetItem* pTempItem = new QTableWidgetItem("张三");
pTempItem->setTextAlignment(Qt::AlignCenter);
m_pTable->setItem(0, 0, pTempItem);

QComboBox *pCombox = new QComboBox();
pCombox->addItem("男");
pCombox->addItem("女");
pCombox->setCurrentIndex(1);
m_pTable->setCellWidget(0, 1, pCombox);
```

## 隐藏表格中的某一列
``` C++
hideColumn(1);
```

## 禁止编辑某些项
``` C++
QTableWidgetItem* pItem = new QTableWidgetItem();
pItem->setFlags(pItem->flags() & (~Qt::ItemIsEditable));
```