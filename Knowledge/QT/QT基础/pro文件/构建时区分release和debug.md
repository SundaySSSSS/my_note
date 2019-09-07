# 构建时区分release和debug
```
CONFIG(debug, debug|release) {

} else {

}
```
注意: { 和 } 必须要按照上面的方式书写, 否则会不起作用, 不能独立作为一行出现