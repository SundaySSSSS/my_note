# Python文本加密
``` Python
import base64

s = "cxy"
bs = base64.b64encode(s)
bs = base64.b64encode(s)
encoded = binascii.b2a_base64(s, newline=False)
bs = base64.b64encode(s.encode("utf-8"))
print(bs)
# b'Y3h5'
decode = base64.b64decode(bs)
print(decode)
# b'cxy'
```