# usage:
# python decode-base64.py encode-file.txt origin-file.txt

import sys
import base64

src_file = sys.argv[1]
dst_file = sys.argv[2]

with open(src_file, 'rb') as file_object:
    contents = file_object.read()
    # print(contents)
    encodeTxt = base64.b64decode(contents)
    with open(dst_file, 'wb') as dst_file_object:
        dst_file_object.write(encodeTxt)
        dst_file_object.close()
    file_object.close()
