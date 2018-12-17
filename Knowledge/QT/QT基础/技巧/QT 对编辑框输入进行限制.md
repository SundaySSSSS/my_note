# QT 对编辑框输入进行限制

``` C++
 QValidator *validator = new QIntValidator(100, 999, this);
  QLineEdit *edit = new QLineEdit(this);

  // the edit lineedit will only accept integers between 100 and 999
  edit->setValidator(validator);
```
其他类型的Validator类似