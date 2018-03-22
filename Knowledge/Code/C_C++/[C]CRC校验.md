# [C]CRC校验

很多网络协议都用到CRC校验码，当自己编写网络协议的时候，也需要编写相应的CRC代码，来进行校验，网上有很多类似的代码，但是有些很麻烦，也不一定高效，我现在提供一个很高效，也很容易理解的CRC校验方法，希望能够对大家有所帮助。
```
//这个函数是用来进行位运算的，主要为下面的计算CRC来服务
int calcByte(int crc, char b)
{
     int i;
 crc = crc ^ (int)b << 8;

    for ( i = 0; i < 8; i++)
    {
        if ((crc & 0x8000) == 0x8000)
            crc = crc << 1 ^ 0x1021;
        else
            crc = crc << 1;
    }
 
    return crc & 0xffff;
}

```

这个函数是计算16位CRC码的函数，只要给出要校验的数组，以及数组长度，就可以返回16位CRC校验码

```
int CRC16(char *pBuffer, int length)
{
    int wCRC16=0;
    int i;
    if (( pBuffer==0 )||( length==0 ))
    {
        return 0;
    }
    for ( i = 0; i < length; i++)
    {
        wCRC16 = calcByte(wCRC16, pBuffer[i]);
    }
    return wCRC16;
}
```

下面这个函数是计算32位CRC码的函数，传入参数是数组，以及校验的数据数量，返回32位的CRC校验码

```
long CRC32(char*  pBuffer, long  length)
{
    long dwCRC32=0;
    if ((NULL == pBuffer)||(0 == length))
    {
        return 0;
    }
    for (int i = 0; i < length; i++)
    {
        dwCRC32 -= *pBuffer++;
    }
    return dwCRC32;
}
```