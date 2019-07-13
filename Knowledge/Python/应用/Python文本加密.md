# Python文本加密
## 原理性代码
``` Python
import base64

s = "cxy"
bs = base64.b64encode(s.encode("utf-8"))
print(bs)
# b'Y3h5'
decode = base64.b64decode(bs)
print(decode)
# b'cxy'
```

## 应用代码, 对文本文件进行加密解密
见附件