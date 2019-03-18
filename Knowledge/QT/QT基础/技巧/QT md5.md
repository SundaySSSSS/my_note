# QT md5

使用QCryptographicHash可以很方便的实现

``` C++
QByteArray input = ui->lineEdit_input->text().toLatin1();
QByteArray output = QCryptographicHash::hash(input, QCryptographicHash::Md5);
ui->lineEdit_output->setText(output.toHex());
```