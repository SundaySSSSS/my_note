# YUV格式的转化

## YUVUV格式转YUV
YUVUV即YYYYYYYYYYYYYYYYUVUVUVUV的格式
YUV即YYYYYYYYYYYYYYYYUUUUVVVV格式
经过测试可用

``` C++
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef unsigned char byte;


int readFile( const char* path, byte* data, size_t len )
{
	printf("read file: %s\n", path);
	FILE* fp = fopen(path, "rb");
	int read_len = 0;
	if (fp != NULL)
	{
		read_len = fread(data, len, 1, fp);
		fclose(fp);
	}
	else
	{
		read_len = -1;
	}
	return read_len;
}

int saveFile( const char* path, byte* data, size_t len )
{
	FILE* fp = fopen(path, "wb");
	if (fp == NULL)
	{
		return -1;
	}
	fwrite(data, len, 1, fp);
	fclose(fp);
	return 0;
}

int YUVUVtoYUV( byte* YUVUV, byte* YUV, int width, int height )
{
	size_t YUV_size = width * height * 3 / 2;
	size_t Y_size = width * height;
	size_t U_size = Y_size / 4;
	size_t V_size = U_size;

	memset(YUV, 0, YUV_size);
	/* 拷贝Y数据 */
	memcpy(YUV, YUVUV, Y_size);

	/* 整理UV数据, 令指针p_walk_UVUV在YUVUV上依次移动, 将UV数据依次取出, 放到YUV中的合适位置 */
	byte* p_walk_UVUV = YUVUV + Y_size;
	byte* p_walk_stop_UVUV = YUVUV + Y_size + U_size + V_size;	//在YUVUV上遍历停止条件
	byte* p_walk_U = YUV + Y_size;
	byte* p_walk_V = YUV + Y_size + U_size;

	do 
	{
		if ((p_walk_UVUV - YUVUV - Y_size) % 2 == 0)
		{	//处理U分量
			*p_walk_U = *p_walk_UVUV;
			p_walk_U++;
		}
		else
		{	//处理V分量
			*p_walk_V = *p_walk_UVUV;
			p_walk_V++;
		}
		p_walk_UVUV++;
	}
	while(p_walk_UVUV != p_walk_stop_UVUV);
	return 0;
}


int main(int argc, char* argv[])
{
	//usage: a.out pic.yuv 1920 1080
	if (argc == 4 && argv[1] != NULL && argv[2] != NULL && argv[3] != NULL)
	{
		int w = atoi(argv[2]);
		int h = atoi(argv[3]);
		size_t len = w * h * 3 / 2;
		byte* yuvuv = (byte*)malloc(len);
		byte* yuv = (byte*)malloc(len);
		printf("preparing...\n");
		if (yuvuv == NULL || yuv == NULL)
		{
			printf("malloc error\n");
			if (yuvuv != NULL) free(yuvuv);
			if (yuv != NULL) free(yuv);
			return -1;
		}
		memset(yuvuv, 0, len);
		memset(yuv, 0, len);
		if (readFile(argv[1], yuvuv, len) < 0)
		{
			printf("read origin yuv error\n");
			return -1;
		}
		YUVUVtoYUV(yuvuv, yuv, w, h);
		saveFile("temp.yuv", yuv, len);
		free(yuvuv);
		return 0;
	}
	else
		return -1;
}



```


