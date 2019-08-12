# SDL_L6_裁剪图片
核心代码
```C++
//将source的clip指定的部分拷贝到destination上的x, y坐标处
//当clip给NULL时, 默认不会进行裁剪
void apply_surface( int x, int y, SDL_Surface* source, SDL_Surface* destination, 
					SDL_Rect* clip = NULL )
{
    //用于保存坐标
    SDL_Rect offset;
    
    //获得坐标
    offset.x = x;
    offset.y = y;
    
    //Blit操作
    SDL_BlitSurface( source, clip, destination, &offset );
}

	//clip的值可以如下:
	SDL_Rect clip[ 4 ];
	//左上角的剪切区域
    clip[ 0 ].x = 0;
    clip[ 0 ].y = 0;
    clip[ 0 ].w = 100;
    clip[ 0 ].h = 100;
    
    //右上角的剪切区域
    clip[ 1 ].x = 100;
    clip[ 1 ].y = 0;
    clip[ 1 ].w = 100;
    clip[ 1 ].h = 100;
    
    //左下角的剪切区域
    clip[ 2 ].x = 0;
    clip[ 2 ].y = 100;
    clip[ 2 ].w = 100;
    clip[ 2 ].h = 100;
    
    //右下角的剪切区域
    clip[ 3 ].x = 100;
    clip[ 3 ].y = 100;
    clip[ 3 ].w = 100;
    clip[ 3 ].h = 100;
```