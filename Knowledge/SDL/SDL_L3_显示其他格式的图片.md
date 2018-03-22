# SDL_L3_显示其他格式的图片
加载SDL_image后, 可以使用`IMG_LOAD`来进行多种图片格式的显示
``` C++
#include <SDL/SDL_image.h>

SDL_Surface *load_image( std::string filename ) 
{
    //临时的空间，用于存储刚刚加载好的图像
    SDL_Surface* loadedImage = NULL;

    //优化后的图像，实际使用的是这个图像
    SDL_Surface* optimizedImage = NULL;
    //加载图像
    loadedImage = IMG_Load( filename.c_str() );
    //如果加载图片没有出错
    if( loadedImage != NULL )
    {
        //创建一个优化了的图像
        optimizedImage = SDL_DisplayFormat( loadedImage );

        //释放临时的图像
        SDL_FreeSurface( loadedImage );
    }
    //返回优化后的表面
    return optimizedImage;
}
```