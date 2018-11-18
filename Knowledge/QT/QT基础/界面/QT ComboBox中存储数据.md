# QT ComboBox中存储数据
ComboxBox中, 的每一项, 如果存储数据, 可以直接在选择某个项目后取得, 非常方便
在添加项目时:
```C++
ui->comboBoxScale->addItem("10m", 10);
ui->comboBoxScale->addItem("30m", 30);
ui->comboBoxScale->addItem("50m", 50);
ui->comboBoxScale->addItem("100m", 100);
ui->comboBoxScale->addItem("1km", 1000);
ui->comboBoxScale->addItem("10km", 10000);
```

之后取得数据:
```C++
QVariant temp = ui->comboBoxScale->itemData(ui->comboBoxScale->currentIndex());
int data = temp.toInt();
```