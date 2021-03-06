# C++大小端转换
``` C++
#include <assert.h>

//16位的转化
template <typename T16>
T16 swap16(const T16 &v)
{
	assert(sizeof(T16) == 2);
	return ((v & 0xff) << 8) | (v >> 8);
}

//32位的转化
template <typename T32>
T32 swap32(const T32 &v)
{
	assert(sizeof(T32) == 4);
 
	return (v >> 24)
		| ((v & 0x00ff0000) >> 8)
		| ((v & 0x0000ff00) << 8)
		| (v << 24);
}

//64位的转化
template <typename T64>
T64 swap64(const T64 &v)
{
	assert(sizeof(T64) == 8);
 
	return (v >> 56)
		| ((v & 0x00ff000000000000) >> 40)
		| ((v & 0x0000ff0000000000) >> 24)
		| ((v & 0x000000ff00000000) >> 8)
		| ((v & 0x00000000ff000000) << 8)
		| ((v & 0x0000000000ff0000) << 24)
		| ((v & 0x000000000000ff00) << 40)
		| (v << 56);
}

//任意位的转化, 效率较低
template <typename T>
T swap(const T &v)
{
	T r;
	int size 			= sizeof(v);
	const unsigned char *cvi 	= (const unsigned char*)&v;
	unsigned char *cri 		= (unsigned char*)&r;
	cri 				= cri + size -1;
	for (int i = 0; i < size; ++i)
	{
		*cri = *cvi;
		++cvi;
		--cri;
	}
 
	return r;
}

void EndianSwap(uint8 *pData, int startIndex, int length)
{
    if (length <= 1)
    {
        return;
    }

    int i,cnt,end,start;
    cnt = length / 2;
    start = startIndex;
    end  = startIndex + length - 1;
    uint8 tmp;
    for (i = 0; i < cnt; i++)
    {
        tmp            = pData[start+i];
        pData[start+i] = pData[end-i];
        pData[end-i]   = tmp;
    }
}

```